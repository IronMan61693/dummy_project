from PyQt5.QtWidgets import QWidget, QStackedWidget, QMessageBox, QInputDialog
from PyQt5.QtCore import pyqtSignal

from character_create import CharacterCreateWidget
from base_graphic_worldtile import BaseGraphicWorldTileWidget

from Game import playClass
from database import DataBase



"""
QWidget is the base class for the central widget
QHBoxLayout and QVBoxLayout are layout classes, H puts in widgets left to right and V Top to bottom
QLabel allows for graphical text boxes
QPushButton class for pushable buttons
QSizePolicy class to dynamically resize, used in Label
QDate class which gives calendar dates
QTime class that allows clock time
QDateTime a class of both QDate and QTime
QLineEdit allows QLineEdit which is allows typing of text
"""
# # Subclassing QThread
# # http://qt-project.org/doc/latest/qthread.html
# class AThread(QThread):

#     def run(self):
#         count = 0
#         while count < 5:
#             time.sleep(1)
#             print("A Increasing")
#             count += 1



class CentralWidget(QWidget):
	"""
	Making a class from the QWidget class, specify variables and behavior 

	Variables:
		mainLayout <QVBoxLayout>
		nameAndDateLayout <QHBoxLayout>
		interactionLayout <QVBoxLayout>
		attributeInventoryLayout <QHBoxLayout>
		attributeLayout <QVBoxLayout>
		comboBoxesFormLayout <QFormLayout>
		nameLabel <QLabel>
		dateTimeLabel <QLabel>
		difficultyLabel <QLabel>
		strengthLabel <QLabel>
		dexterifyLabel <QLabel>
		constitutionLabel <QLabel>
		intellectLabel <QLabel>
		inventoryLabel <QLabel>
		nameLineEdit <QLineEdit>
		classSelectorComboBox <QComboBox>
		difficultyComboBox <QComboBox>
		finishPushButton <QPushButton>

	Methods:
		classChange
		difficultyChange
		finishChange
		nameChange
		
	"""
	procShowMenu = pyqtSignal()

	def __init__(self):

		super().__init__()

		self.Stack = QStackedWidget(self)
		self.characterCreateWidget = CharacterCreateWidget()
		self.baseGraphicWorldTileWidget = BaseGraphicWorldTileWidget()

		self.game = playClass()

		self.database = DataBase("engine.db")
		self.createTables()

		self.characterCreateWidget.procGameStart.connect(self.startGame)
		self.characterCreateWidget.procCharLabel.connect(self.baseGraphicWorldTileWidget.set_player_image)
		


		self.Stack.addWidget (self.characterCreateWidget)
		self.Stack.addWidget (self.baseGraphicWorldTileWidget)





	def startGame(self, index, character_class_name, character_name, player_name):
		self.Stack.setCurrentIndex(index)
		self.game.change_player_info(character_class_name, character_name, player_name)
		self.editInteractableTile()
		self.procShowMenu.emit()




	def keyPressEvent (self, event):
		super().keyPressEvent
		if not (event.modifiers()):
			self.userInputAction(event.text())
			self.game.doAction()
			self.editInteractableTile()
			if (event.text() == "c"):
				self.showCharacterInfo()
			if (event.text() == "i"):
				self.showInventoryInfo()
			if (event.text() == "o"):
				self.changeEquipmentGeneral()


		else:
			self.game.setNotMoved()
		


	def userInputAction(self, actionString):

		self.game.setUserAction(actionString)



	def editInteractableTile(self):
		self.game.enterRoom()

		self.tileDescription = self.game.getTileDescription()
		self.actionDescription = self.game.getAvailableActions()


		self.roomType = self.game.getTypeOfRoom()
		# Return 0 if empty
		# Return 1 if loot room with lootable
		# Return 2 if loot room already looted
		# Return 3 if ogre room with active enemy
		# Return 4 if ogre killed
		# Return 5 if spider active
		# 6 if spider dead
		if (self.roomType == 0):
			self.baseGraphicWorldTileWidget.empty_room()

		elif (self.roomType == 1):
			self.baseGraphicWorldTileWidget.active_loot()

		elif (self.roomType == 2):
			self.baseGraphicWorldTileWidget.room_looted()

		elif (self.roomType == 3):
			self.baseGraphicWorldTileWidget.active_ogre()

		elif (self.roomType == 4):
			self.baseGraphicWorldTileWidget.dead_ogre()

		elif (self.roomType == 5):
			self.baseGraphicWorldTileWidget.active_spider()

		elif (self.roomType == 6):
			self.baseGraphicWorldTileWidget.dead_spider()


		self.baseGraphicWorldTileWidget.set_room_description(self.tileDescription, self.game.getMoved(),\
															 self.actionDescription)



	def showRoomDesc(self):
		self.baseGraphicWorldTileWidget.set_room_description(self.tileDescription, True, self.actionDescription)

	def showAvailActions(self):
		self.baseGraphicWorldTileWidget.set_actions(self.actionDescription)

	def showCharacterInfo(self):
		charInfo = self.game.submitGameInfo()
		charInfoString = "Player: " + str(charInfo[0]) + "\n" + \
						 "Character: " + str(charInfo[1]) + "\n" + \
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
		equipmentSlots = ("MainHand", "OffHand", "Armor", "Ring", "Amulet")
		equipmentSlot, okPressed = QInputDialog.getItem(self, "Choose Slot", "Equipment Slot:", equipmentSlots, 0, False)
		if okPressed:
			if equipmentSlot == "MainHand":
				self.changeEquipmentMainHand()

	def changeEquipmentMainHand(self):

		mainHandSlots = tuple(self.game.mainHandOptions())
		mainHandSlot, okPressed = QInputDialog.getItem(self, "Choose Item", "Weapons Available:", mainHandSlots, 0, False)
		if okPressed:
			self.game.equipMainHand(mainHandSlot)


	def unstuckCharacter(self):
		self.game.unstickCharacter()


	def showHelpfulInfo(self):
		helpfulString = ("Welcome to a super cool RPG\n"
						 "Everything you could ever need to know can be found in this menu bar. "
						 "File includes an option to upload your current game to the website. "
						 "Save and Load do not work at this time, and Exit will quit the game. "
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
		# First get the information I want from the game state
		# Information I want: player_name, charactername, level, tiles, class
		# Creating a method in game that will send all that information as a tuple
		current_game_info = self.game.submitGameInfo()

		command_upload_current = ("INSERT INTO gameInfo VALUES (?,?,?,?,?);")

		self.database.execute(command_upload_current, current_game_info)

		#Then the SQL commands to put that information into the database

