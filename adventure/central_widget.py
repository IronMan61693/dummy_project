import webbrowser


from PyQt5.QtWidgets import QWidget, QStackedWidget, QMessageBox, QInputDialog
from PyQt5.QtCore import pyqtSignal, Qt

from character_create import CharacterCreateWidget
from base_graphic_worldtile import BaseGraphicWorldTileWidget

from Game import playClass
from database import DataBase


class CentralWidget(QWidget):
	"""
	Making a class from the QWidget class, specify variables and behavior 

	Variables:
		procShowMenu <pyqtSignal>
		Stack <QStackedWidget>
		characterCreateWidget <CharacterCreateWidget>
		baseGraphicWorldTileWidget <BaseGraphicWorldTileWidget>

		game <playClass>
		database <DataBase>

		
	Methods:
		startGame() Changes stack index, sends information to the game from the character create, sets update message box
		keyPressEvent() Overrides QT keyPressEvent handler
		userInputAction() Uses game setUserAction
		editInteractableTable() Changes the look of the baseGraphicTile depending on the state of the game
		showRoomDesc() Uses set baseGraphic set_room_description, shows message box
		showAvailActions() Uses baseGraphic to show action messagebox
		showCharacterInfo() Uses messagebox to display character information
		showInventoryInfo() Uses messagebox to display inventory information
		changeEquipmentGeneral() Uses InputDialog to choose which equipment slot to update in the game
		changeEquipmentMainHand() Uses InputDialog to change mainhand equipped in game
		unstuckCharacter() Uses game unstickCharacter and displays a message box to inform the character
		showHelpfulInfo() Uses messagebox to display useful UI information.
		createTables() Uses sqlite to initialize tables in db if they do not exist already
		uploadGameInfo() Uses sqlite to upload character information to engine.db	
		launchWeb() Uses webbrowser to open the website at the base url	
		launchWebTopScore() Uses webbrowser to open the website at the top score url	
	"""
	procShowMenu = pyqtSignal()

	def __init__(self):

		super().__init__()

		######################################################################################################
		# Creating the parts of the stack and the stack itself
		######################################################################################################

		self.Stack = QStackedWidget(self)
		self.characterCreateWidget = CharacterCreateWidget()
		self.baseGraphicWorldTileWidget = BaseGraphicWorldTileWidget()

		self.game = playClass()

		self.database = DataBase("engine.db")
		self.createTables()

		######################################################################################################
		# Connecting signals
		######################################################################################################

		self.characterCreateWidget.procGameStart.connect(self.startGame)
		self.characterCreateWidget.procCharLabel.connect(self.baseGraphicWorldTileWidget.set_player_image)

		self.baseGraphicWorldTileWidget.displayActionPushButton.clicked.connect(self.showAvailActions)
		
		######################################################################################################
		# re-Parenting Stack
		######################################################################################################

		self.Stack.addWidget (self.characterCreateWidget)
		self.Stack.addWidget (self.baseGraphicWorldTileWidget)





	def startGame(self, index, character_class_name, character_name, player_name):
		"""
		Changes stack index, provides information from the characterCreateWidget to the game
		 displays a MessageBox with game related update information

		Input:
			index <int>
			character_class_name <str>
			character_name <str>
			player_name <str>
		"""
		self.Stack.setCurrentIndex(index)
		self.game.change_player_info(character_class_name, character_name, player_name)
		self.editInteractableTile()
		self.procShowMenu.emit()


		updateInfoString =  ("We are currently aware of the following bugs:\n\n\n"
							 "Upon completing battle the player must click a keyboard key in order to update the room.\n"
							 ) 


		updateInfoMessageBox = QMessageBox()
		updateInfoMessageBox.setIcon(QMessageBox.Information)
		updateInfoMessageBox.setText(updateInfoString)
		updateInfoMessageBox.setWindowTitle("Future Updates")
		updateInfoMessageBox.setStandardButtons(QMessageBox.Ok)

		updateInfoMessageBox.exec_()




	def keyPressEvent (self, event):
		"""
		Overrides QT keyPressEvent with useful methods from this widget, used to display information

		Input:
			event <QEvent>
		"""
		super().keyPressEvent

		if not (event.modifiers()):
			if event.key() ==  Qt.Key_Space:
				print("keyPress space")
			self.userInputAction(event.text())
			self.game.doAction()
			self.editInteractableTile()
			if (event.text() == "c"):
				self.showCharacterInfo()
			if (event.text() == "i"):
				self.showInventoryInfo()
			if (event.text() == "o"):
				self.changeEquipmentGeneral()

			if self.game.inCombat():
				self.baseGraphicWorldTileWidget.append_scrolling_info(self.game.enemyCombatInformation())


		else:
			self.game.setNotMoved()
		


	def userInputAction(self, actionString):
		"""
		Used to call game method setUserAction and provides the key pressed as a string

		Input:
			actionString <str>
		"""
		self.game.setUserAction(actionString)



	def editInteractableTile(self):
		"""
		Changes the look of the baseGraphicTile depending on the state of the game.
		 Uses game methods to pull information from the game and updates appropriately 
		"""
		self.game.enterRoom()

		self.tileDescription = self.game.getTileDescription()
		self.actionDescription = self.game.getAvailableActions()
		if self.game.inCombat():
			self.baseGraphicWorldTileWidget.append_scrolling_info(self.game.combatInformation())


		self.roomType = self.game.getTypeOfRoom()
		# Return 0 if empty
		# Return 1 if loot room with lootable
		# Return 2 if loot room already looted
		# Return 3 if enemy defeated
		# Return 4 if ogre 
		# Return 5 if spider 
		# Return 6 if bandit
		# Return 7 if valkyrie
		# Return 8 if assassin
		# Return 9 if deathknight
		# Return 10 if giant
		# Return 11 if greendragon
		# Return 12 if wizard

		if (self.roomType == 0):
			self.baseGraphicWorldTileWidget.empty_room()

		elif (self.roomType == 1):
			self.baseGraphicWorldTileWidget.active_loot()

		elif (self.roomType == 2):
			self.baseGraphicWorldTileWidget.room_looted()

		elif (self.roomType == 3):
			self.baseGraphicWorldTileWidget.defeated_enemy()

		elif (self.roomType == 4):
			self.baseGraphicWorldTileWidget.active_ogre()

		elif (self.roomType == 5):
			self.baseGraphicWorldTileWidget.active_spider()

		elif (self.roomType == 6):
			self.baseGraphicWorldTileWidget.active_bandit()

		elif (self.roomType == 7):
			self.baseGraphicWorldTileWidget.active_valkyrie()

		elif (self.roomType == 8):
			self.baseGraphicWorldTileWidget.active_assassin()

		elif (self.roomType == 9):
			self.baseGraphicWorldTileWidget.active_deathknight()

		elif (self.roomType == 10):
			self.baseGraphicWorldTileWidget.active_giant()

		elif (self.roomType == 11):
			self.baseGraphicWorldTileWidget.active_greendragon()

		elif (self.roomType == 12):
			self.baseGraphicWorldTileWidget.active_wizard()

		
		elif (self.roomType == -1):
			self.baseGraphicWorldTileWidget.empty_room()
			GameOverString = ("Game Over!\n"
							  "Remember under File you can upload this character to the website for others to see how"
							  " far you have made it! Click Ok to view the leaderboard")

			GameOverMessageBox = QMessageBox()
			GameOverMessageBox.setIcon(QMessageBox.Critical)
			GameOverMessageBox.setText(GameOverString)
			GameOverMessageBox.setWindowTitle("GAME OVER")
			GameOverMessageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

			gameOverReply = GameOverMessageBox.exec_()

			if (gameOverReply == QMessageBox.Ok):
				self.launchWebTopScore()
				print("Ok")

			
		self.baseGraphicWorldTileWidget.set_room_description(self.tileDescription, self.game.getMoved(),\
															 self.actionDescription)



	def showRoomDesc(self):
		"""
		Uses baseGraphicWorldTileWidget method set_room_description in order to pull up associated messagebox
		"""
		self.baseGraphicWorldTileWidget.set_room_description(self.tileDescription, True, self.actionDescription)

	def showAvailActions(self):
		"""
		Uses baseGraphicWorldTileWidget method set_actions in order to pull up associated messagebox
		"""
		self.baseGraphicWorldTileWidget.set_actions(self.actionDescription)

	def showCharacterInfo(self):
		"""
		Uses QMessageBox to display character information pulled from game
		"""
		charInfo = self.game.submitGameInfo()
		charInfoString = "Player: " + str(charInfo[0]) + "\n" + \
						 "Character: " + str(charInfo[1]) + "\n" + \
						 "Health Points: " + str(self.game.player.hp) + "\n" + \
						 "Class: " + str(charInfo[2]) + "\n" + \
						 "Level: " + str(charInfo[3]) + "\n" + \
						 "Total Tiles: " + str(charInfo[4]) 

		charInfoMessageBox = QMessageBox()
		charInfoMessageBox.setIcon(QMessageBox.Question)
		charInfoMessageBox.setText(charInfoString)
		charInfoMessageBox.setWindowTitle("Your Information")
		charInfoMessageBox.setStandardButtons(QMessageBox.Ok)

		charInfoMessageBox.exec_()


	def showInventoryInfo(self):
		"""
		Uses QMessageBox to display inventory information pulled from game
		"""
		inventoryInfo = self.game.currentInventoryDictionary()
		equippedInfo = self.game.currentEquippedAll()
		inventoryInfoString = "Current Inventory \n"
		for item, amount in inventoryInfo.items():
			inventoryInfoString = (inventoryInfoString + "Item: " + item.name + " Quantity: " + str(amount) + "\n")
			inventoryInfoString = (inventoryInfoString + item.description + "\n")
		inventoryInfoString = inventoryInfoString + "Currently equipped: \n"
		for equipped in equippedInfo:
			if equipped is not None:
				inventoryInfoString = (inventoryInfoString + equipped.name + "\n")


		invInfoMessageBox = QMessageBox()
		invInfoMessageBox.setIcon(QMessageBox.Question)
		invInfoMessageBox.setText(inventoryInfoString)
		invInfoMessageBox.setWindowTitle("Your Inventory")
		invInfoMessageBox.setStandardButtons(QMessageBox.Ok)

		invInfoMessageBox.exec_()



	def changeEquipmentGeneral(self):
		"""
		Uses QInputDialog to choose which equipment slot to update in the game
		"""
		equipmentSlots = (["MainHand", "Armor"])
		# , "OffHand", "Armor", "Ring", "Amulet"
		equipmentSlot, okPressed = QInputDialog.getItem(self, "Choose Slot", "Equipment Slot:", equipmentSlots, 0, False)
		if okPressed:
			if equipmentSlot == "MainHand":
				self.changeEquipmentMainHand()
			elif equipmentSlot == "Armor":
				self.changeEquipmentArmor()

	def changeEquipmentMainHand(self):
		"""
		Uses QInputDialog to choose which item to equip in the mainhand and update in the game
		"""
		mainHandSlots = tuple(self.game.mainHandOptions())
		mainHandSlot, okPressed = QInputDialog.getItem(self, "Choose MainHand", "Weapons Available:", mainHandSlots, 0, False)
		if okPressed:
			self.game.equipMainHand(mainHandSlot)

	def changeEquipmentArmor(self):
		"""
		Uses QInputDialog to choose which item to equip for armor and update in the game
		"""
		armorSlots = tuple(self.game.armorOptions())
		armorSlot, okPressed = QInputDialog.getItem(self, "Choose Armor", "Armor Available:", armorSlots, 0, False)
		if okPressed:
			self.game.equipArmor(armorSlot)

	def unstuckCharacter(self):
		"""
		Uses game unstickCharacter and displays a message box to inform the character
		"""
		self.game.unstickCharacter()
		unstickString = ("With a bang and a whir you have teleported to a new location!")

		unstickMessageBox = QMessageBox()
		unstickMessageBox.setIcon(QMessageBox.Critical)
		unstickMessageBox.setText(unstickString)
		unstickMessageBox.setWindowTitle("UNSTUCK")
		unstickMessageBox.setStandardButtons(QMessageBox.Ok)

		unstickMessageBox.exec_()


	def showHelpfulInfo(self):
		"""
		Uses QMessageBox to display useful UI information.
		"""
		helpfulString = ("Welcome to a super cool RPG\n"
						 "Everything you could ever need to know can be found in this menu bar. "
						 "File includes an option to upload your current game to the website. "
						 "Character contains useful buttons for your character, inventory and equipment. "
						 "Help provides information on your current room, the keyboard actions you can currently take "
						 "and the stuck button will teleport you to a random location in the case that the doors get you stuck.")
		helpfulMessageBox = QMessageBox()
		helpfulMessageBox.setIcon(QMessageBox.Information)
		helpfulMessageBox.setText(helpfulString)
		helpfulMessageBox.setWindowTitle("Help")
		helpfulMessageBox.setStandardButtons(QMessageBox.Ok)

		helpfulMessageBox.exec_()




	def createTables(self):
		"""
		Uses sqlite to initialize tables in db if they do not exist already
		"""
		command_string_gameInfo =("CREATE TABLE IF NOT EXISTS gameInfo"
								  " (player_name text NOT NULL,"
								  " character_name text NOT NULL,"
								  " class text NOT NULL,"
								  " level integer NOT NULL,"
								  " tiles integer NOT NULL);"
								 )
		command_string_webInfo =("CREATE TABLE IF NOT EXISTS webInfo"
								 " (user_name text NOT NULL,"
								 " password_hash text NOT NULL);"
								)
		command_list = [command_string_gameInfo, command_string_webInfo]

		self.database.execute(command_list)



	def uploadGameInfo(self):
		"""
		Uses sqlite to upload character information to engine.db, gets the information from the game state:
		 player_name, charactername, level, tiles, class
		 A method in game sends all that information as a tuple
		"""
		current_game_info = self.game.submitGameInfo()

		command_upload_current = ("INSERT INTO gameInfo VALUES (?,?,?,?,?);")

		self.database.execute(command_upload_current, current_game_info)


	def launchWeb(self):
		""" 
		The website is opened up in the users default browser
		"""
		webbrowser.open_new("http://127.0.0.1:5000")

	def launchWebTopScore(self):
		""" 
		The website is opened up in the users default browser
		"""
		webbrowser.open_new("http://127.0.0.1:5000/score")