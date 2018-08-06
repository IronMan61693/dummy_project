from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QMessageBox, QPlainTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage, QKeyEvent

from character_create import CharacterCreateWidget




class BaseGraphicWorldTileWidget (QWidget):
	"""
	The visual representation of the game state

	Variables:
		mainLayout <QVBoxLayout>
		gameBorderFrame <QFrame>
		addUsefulLayout <QHBoxLayout>
		mainInnerLayout <QVBoxLayout>
		topInnerLayout <QVBoxLayout>
		middleInnerLayout <QHBoxLayout>
		bottomInnerLayout <QVBoxLayout>
		rightSideLayout <QVBoxLayout
		holdCharacterInteractionLayout <QVBoxLayout

		playerLabel <QLabel>
		interactableLabel <QLabel>
		topDoorLabel <QLabel>
		leftDoorLabel <QLabel>
		rightDoorLabel <QLabel>
		bottomDoorLabel <QLabel>

		scrollingInfoProvidingPlainTextEdit <QPlainTextEdit>
		introTextString <str>

		displayActionPushButton <QPushButton>

		doorImage <QImage>
		doorPixmap <QPixmap>

	Methods:
		set_player_image() Changes the look of the player label based on resourcePath
		set_room_description() Causes a MessageBox explaining the room if the player has moved
		

	"""

	def __init__(self):
		super().__init__()

		######################################################################################################
		# Creating Layouts
		######################################################################################################

		self.mainLayout = QVBoxLayout(self)

		
		self.gameBorderFrame = QFrame()
		
		self.gameBorderFrame.setFrameStyle(QFrame.Box)
		self.gameBorderFrame.setStyleSheet("background-color: rgb(147,145,150)")
		self.gameBorderFrame.setMinimumWidth(560)
		self.gameBorderFrame.setMinimumHeight(580)

		self.addUsefulLayout = QHBoxLayout(self.gameBorderFrame)

		self.mainInnerLayout = QVBoxLayout()
		self.topInnerLayout = QVBoxLayout()
		self.middleInnerLayout = QHBoxLayout()
		self.bottomInnerLayout = QVBoxLayout()

		self.rightSideLayout = QVBoxLayout()

		self.holdCharacterInteractionLayout = QVBoxLayout()
	

		######################################################################################################
		# Creating Labels and TextEdit
		######################################################################################################

		self.playerLabel = QLabel()
		self.playerLabel.setText("Player")

		self.interactableLabel = QLabel()
		self.interactableLabel.setText("Interaction")
		self.interactableLabel.hide()

		self.topDoorLabel = QLabel()
		self.leftDoorLabel = QLabel()
		self.rightDoorLabel = QLabel()
		self.bottomDoorLabel = QLabel()


		self.scrollingInfoProvidingPlainTextEdit = QPlainTextEdit()
		self.scrollingInfoProvidingPlainTextEdit.setFixedWidth(230)
		self.scrollingInfoProvidingPlainTextEdit.setReadOnly(True)
		self.introTextString = ("Greetings adventurer\n"
								"Here you will find useful information regarding the game you are currently playing.\n"
								"The actions you can take can be found under the help button on the menu.\n"
								"The Help button will also give you some further information regarding what exactly is going on.\n"
								"Right now I would recommend clicking i to look at your inventory.\n"
								"You can also click c to look at your character.\n"
								"Currently you may click w,a,s,d in order to go in the corresponding direction.\n"
								"North East South and West respectively.\n"
								"If doors do not appear click an action to refresh the page, i or c etc.\n")
		self.scrollingInfoProvidingPlainTextEdit.appendPlainText(self.introTextString)

		self.displayActionPushButton = QPushButton("Actions!")

		######################################################################################################
		# Setting images to the door labels
		######################################################################################################

		self.doorImage = QImage("resources/Door.png")
		self.doorImage = self.doorImage.scaled(35,35)

		self.doorPixmap = QPixmap(self.doorImage)

		self.topDoorLabel.setPixmap(self.doorPixmap)
		self.bottomDoorLabel.setPixmap(self.doorPixmap)
		self.leftDoorLabel.setPixmap(self.doorPixmap)
		self.rightDoorLabel.setPixmap(self.doorPixmap)

		######################################################################################################
		# Aligning Labels and locations of layouts
		######################################################################################################

		self.topDoorLabel.setAlignment(Qt.AlignCenter)
		self.bottomDoorLabel.setAlignment(Qt.AlignCenter)
		self.rightDoorLabel.setAlignment(Qt.AlignRight)
		self.leftDoorLabel.setAlignment(Qt.AlignLeft)
		self.interactableLabel.setAlignment(Qt.AlignCenter)
		self.playerLabel.setAlignment(Qt.AlignCenter)

		self.mainInnerLayout.addStretch(0)
		self.mainInnerLayout.addLayout(self.topInnerLayout)
		self.mainInnerLayout.addStretch(1)
		self.mainInnerLayout.addLayout(self.middleInnerLayout)
		self.mainInnerLayout.addStretch(1)
		self.mainInnerLayout.addLayout(self.bottomInnerLayout)

		######################################################################################################
		# re-Parenting topInnerLayout
		######################################################################################################

		self.topInnerLayout.addWidget(self.topDoorLabel)
		
		######################################################################################################
		# re-Parenting middleInnerLayout
		######################################################################################################

		self.middleInnerLayout.addWidget(self.leftDoorLabel)
		self.middleInnerLayout.addWidget(self.interactableLabel)
		self.middleInnerLayout.addLayout(self.holdCharacterInteractionLayout)
		self.middleInnerLayout.addWidget(self.rightDoorLabel)

		######################################################################################################
		# re-Parenting bottomInnerLayout
		######################################################################################################

		self.bottomInnerLayout.addWidget(self.bottomDoorLabel)	

		######################################################################################################
		# re-Parenting holdCharacterInteractionLayout
		######################################################################################################

		self.holdCharacterInteractionLayout.addWidget(self.interactableLabel)
		self.holdCharacterInteractionLayout.addStretch(1)
		self.holdCharacterInteractionLayout.addWidget(self.playerLabel)

		######################################################################################################
		# re-Parenting rightSideLayout
		######################################################################################################

		self.rightSideLayout.addWidget(self.scrollingInfoProvidingPlainTextEdit)
		self.rightSideLayout.addWidget(self.displayActionPushButton)

		######################################################################################################
		# re-Parenting addUsefulLayout
		######################################################################################################

		# self.mainInnerLayout.addWidget(self.gameBorderFrame)
		self.addUsefulLayout.addLayout(self.mainInnerLayout)
		self.addUsefulLayout.addLayout(self.rightSideLayout)

		######################################################################################################
		# Formatting the main screen
		######################################################################################################

		self.mainLayout.addStretch(1)
		self.mainLayout.addWidget(self.gameBorderFrame)
		self.mainLayout.addStretch(1)




	

	def set_player_image(self, resourcePath):
		"""
		Changes the look of the player label based on resourcePath

		Input:
			resourcePath <str>
		"""
		self.playerImage = QImage(resourcePath)
		self.playerImage = self.playerImage.scaled(50,50)

		self.playerPixmap = QPixmap(self.playerImage)

		self.playerLabel.setPixmap(self.playerPixmap)





	def set_room_description(self, roomDescription, moved, actions):
		"""
		Causes a MessageBox explaining the room if the player has moved

		Input:
			roomDescription <str>
			moved <bool>
			actions <Action>
		"""

		if moved:
			self.roomDescriptionMessageBox = QMessageBox()
			self.roomDescriptionMessageBox.setIcon(QMessageBox.Information)
			self.roomDescriptionMessageBox.setText(roomDescription)
			self.roomDescriptionMessageBox.setWindowTitle("Your current room")
			self.roomDescriptionMessageBox.setStandardButtons(QMessageBox.Ok)

			self.roomDescriptionMessageBox.exec_()


		action_hotkeys = []
		for action in actions:
			action_hotkeys.append(action.hotkey)


		if "w" in action_hotkeys:
			self.topDoorLabel.show()
		else:
			self.topDoorLabel.hide()

		if "d" in action_hotkeys:
			self.rightDoorLabel.show()
		else:
			self.rightDoorLabel.hide()

		if "s" in action_hotkeys:
			self.bottomDoorLabel.show()
		else:
			self.bottomDoorLabel.hide()

		if "a" in action_hotkeys:
			self.leftDoorLabel.show()
		else:
			self.leftDoorLabel.hide()



	def append_scrolling_info(self, infoString):
		"""
		Appends the input string to the plainTextEdit

		Input:
			infoString <str>
		"""
		self.scrollingInfoProvidingPlainTextEdit.appendPlainText(infoString)








	def set_actions(self, actions):
		"""
		Creates a message box describing the available actions.

		Input:
			actions [<str>]
		"""
		self.actionString = "Actions:\n"
		for action in actions:
			self.actionString = self.actionString + str(action) + "\n"

		self.actionsMessageBox = QMessageBox()
		self.actionsMessageBox.setIcon(QMessageBox.Warning)
		self.actionsMessageBox.setText(self.actionString)
		self.actionsMessageBox.setWindowTitle("Available Actions")
		self.actionsMessageBox.setStandardButtons(QMessageBox.Ok)

		self.actionsMessageBox.exec_()


	def empty_room(self):
		"""
		Hides the interactableLabel
		"""

		self.interactableLabel.hide()

	def set_interactableLootLabel(self, imagePath):
		"""
		Shows the interactableLabel with the image found in the resource path (specific for loot)

		Input:
			imagePath <str>
		"""

		self.interactableLabel.show()

		self.lootImage = QImage(imagePath)
		self.lootImage = self.lootImage.scaled(40,40)

		self.lootPixmap = QPixmap(self.lootImage)

		self.interactableLabel.setPixmap(self.lootPixmap)



	def set_interactableEnemyLabel(self, imagePath):
		"""
		Shows the interactableLabel with the image found in the resource path (specific for enemy)

		Input:
			imagePath <str>
		"""

		self.interactableLabel.show()

		self.enemyImage = QImage(imagePath)
		self.enemyImage = self.enemyImage.scaled(90,90)

		self.enemyPixmap = QPixmap(self.enemyImage)

		self.interactableLabel.setPixmap(self.enemyPixmap)
	


	def active_loot(self):
		"""
		Uses set_interactableLootLabel to set the interactableLabel to a closed chest image
		"""

		self.imagePath = "resources/chest.jpeg"
		self.set_interactableLootLabel(self.imagePath)



	def room_looted(self):
		"""
		Uses set_interactableLootLabel to set the interactableLabel to an open chest image
		"""

		self.imagePath = "resources/TreasureChestOpen.png"
		self.set_interactableLootLabel(self.imagePath)



	def active_ogre(self):
		"""
		Uses set_interactableEnemyLabel to set the interactableLabel to an alive ogre image
		"""

		self.imagePath = "resources/OgreAlive.png"
		self.set_interactableEnemyLabel(self.imagePath)

	def dead_ogre(self):
		"""
		Uses set_interactableEnemyLabel to set the interactableLabel to a dead ogre image
		"""

		self.imagePath = "resources/OgreDead.jpg"
		self.set_interactableEnemyLabel(self.imagePath)

	def active_spider(self):
		"""
		Uses set_interactableEnemyLabel to set the interactableLabel to an alive spider image
		"""

		self.imagePath = "resources/SpiderAlive.jpg"
		self.set_interactableEnemyLabel(self.imagePath)

	def dead_spider(self):
		"""
		Uses set_interactableEnemyLabel to set the interactableLabel to an dead spider image
		"""

		self.imagePath = "resources/SpiderDead.png"
		self.set_interactableEnemyLabel(self.imagePath)