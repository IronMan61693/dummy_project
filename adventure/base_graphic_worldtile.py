from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QMessageBox, QPlainTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage, QKeyEvent

from character_create import CharacterCreateWidget




class BaseGraphicWorldTileWidget (QWidget):


	def __init__(self):
		super().__init__()

		

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

		self.holdCharacterInteractionLayout = QVBoxLayout()
	
		
		# self.roomDescriptionLabel = QLabel()
		# self.roomDescriptionLabel.setText("This is where the description of the current mapTile will go")
		# self.roomDescriptionLabel.setWordWrap( True )

		# self.actionsLabel = QLabel()
		# self.actionsLabel.setText("This is where actions go")
		# self.actionsLabel.setWordWrap( True )

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
								"Are you can click n,e,s,w in order to go in that direction.\n"
								"North East South and West respectively.\n")
		self.scrollingInfoProvidingPlainTextEdit.appendPlainText(self.introTextString)

		self.doorImage = QImage("resources/Door.png")
		self.doorImage = self.doorImage.scaled(35,35)

		self.doorPixmap = QPixmap(self.doorImage)

		self.topDoorLabel.setPixmap(self.doorPixmap)
		self.bottomDoorLabel.setPixmap(self.doorPixmap)
		self.leftDoorLabel.setPixmap(self.doorPixmap)
		self.rightDoorLabel.setPixmap(self.doorPixmap)

		
		self.topDoorLabel.setAlignment(Qt.AlignCenter)
		self.bottomDoorLabel.setAlignment(Qt.AlignCenter)
		self.rightDoorLabel.setAlignment(Qt.AlignRight)
		self.leftDoorLabel.setAlignment(Qt.AlignLeft)
		self.interactableLabel.setAlignment(Qt.AlignCenter)
		self.playerLabel.setAlignment(Qt.AlignCenter)
		# self.roomDescriptionLabel.setAlignment(Qt.AlignCenter)
		# self.actionsLabel.setAlignment(Qt.AlignCenter)







		self.mainInnerLayout.addStretch(0)
		self.mainInnerLayout.addLayout(self.topInnerLayout)
		self.mainInnerLayout.addStretch(1)
		self.mainInnerLayout.addLayout(self.middleInnerLayout)
		self.mainInnerLayout.addStretch(1)
		# self.mainInnerLayout.addWidget(self.roomDescriptionLabel)
		# self.mainInnerLayout.addWidget(self.actionsLabel)
		# self.mainInnerLayout.addStretch(0)
		self.mainInnerLayout.addLayout(self.bottomInnerLayout)


		self.topInnerLayout.addWidget(self.topDoorLabel)
		

		self.middleInnerLayout.addWidget(self.leftDoorLabel)
		self.middleInnerLayout.addWidget(self.interactableLabel)
		self.middleInnerLayout.addLayout(self.holdCharacterInteractionLayout)
		self.middleInnerLayout.addWidget(self.rightDoorLabel)

		self.bottomInnerLayout.addWidget(self.bottomDoorLabel)	


		self.holdCharacterInteractionLayout.addWidget(self.interactableLabel)
		self.holdCharacterInteractionLayout.addStretch(1)
		self.holdCharacterInteractionLayout.addWidget(self.playerLabel)



		# self.mainInnerLayout.addWidget(self.gameBorderFrame)
		self.addUsefulLayout.addLayout(self.mainInnerLayout)
		self.addUsefulLayout.addWidget(self.scrollingInfoProvidingPlainTextEdit)

		self.mainLayout.addStretch(1)
		self.mainLayout.addWidget(self.gameBorderFrame)
		self.mainLayout.addStretch(1)




	

	def set_player_image(self, resourcePath):
		self.playerImage = QImage(resourcePath)
		self.playerImage = self.playerImage.scaled(50,50)

		self.playerPixmap = QPixmap(self.playerImage)

		self.playerLabel.setPixmap(self.playerPixmap)





	def set_room_description(self, roomDescription, moved, actions):
		# Change door labels here

		# self.roomDescriptionLabel.setText(roomDescription)

		if moved:
			self.roomDescriptionMessageBox = QMessageBox()
			self.roomDescriptionMessageBox.setIcon(QMessageBox.Information)
			self.roomDescriptionMessageBox.setText(roomDescription)
			self.roomDescriptionMessageBox.setWindowTitle("Your current room")
			self.roomDescriptionMessageBox.setStandardButtons(QMessageBox.Ok)

			self.roomDescriptionMessageBox.exec_()

			self.scrollingInfoProvidingPlainTextEdit.appendPlainText(roomDescription)

		action_hotkeys = []
		for action in actions:
			action_hotkeys.append(action.hotkey)


		if "n" in action_hotkeys:
			self.topDoorLabel.show()
		else:
			self.topDoorLabel.hide()

		if "e" in action_hotkeys:
			self.rightDoorLabel.show()
		else:
			self.rightDoorLabel.hide()

		if "s" in action_hotkeys:
			self.bottomDoorLabel.show()
		else:
			self.bottomDoorLabel.hide()

		if "w" in action_hotkeys:
			self.leftDoorLabel.show()
		else:
			self.leftDoorLabel.hide()




# def showdialog():
#    msg = QMessageBox()
#    msg.setIcon(QMessageBox.Information)

#    msg.setText("This is a message box")
#    msg.setInformativeText("This is additional information")
#    msg.setWindowTitle("MessageBox demo")
#    msg.setDetailedText("The details are as follows:")
#    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msg.buttonClicked.connect(msgbtn)
	
#    retval = msg.exec_()
#    print "value of pressed message box button:", retval




	def set_actions(self, actions):
		self.actionString = "Actions:\n"
		for action in actions:
			self.actionString = self.actionString + str(action) + "\n"

		self.actionsMessageBox = QMessageBox()
		self.actionsMessageBox.setIcon(QMessageBox.Warning)
		self.actionsMessageBox.setText(self.actionString)
		self.actionsMessageBox.setWindowTitle("Available Actions")
		self.actionsMessageBox.setStandardButtons(QMessageBox.Ok)

		self.actionsMessageBox.exec_()
		# self.actionsLabel.setText(self.actionString)


	def empty_room(self):

		self.interactableLabel.hide()

	def set_interactableLootLabel(self, imagePath):

		self.interactableLabel.show()

		self.lootImage = QImage(imagePath)
		self.lootImage = self.lootImage.scaled(40,40)

		self.lootPixmap = QPixmap(self.lootImage)

		self.interactableLabel.setPixmap(self.lootPixmap)



	def set_interactableEnemyLabel(self, imagePath):

		self.interactableLabel.show()

		self.enemyImage = QImage(imagePath)
		self.enemyImage = self.enemyImage.scaled(90,90)

		self.enemyPixmap = QPixmap(self.enemyImage)

		self.interactableLabel.setPixmap(self.enemyPixmap)
	


	def active_loot(self):
		self.imagePath = "resources/chest.jpeg"
		self.set_interactableLootLabel(self.imagePath)



	def room_looted(self):

		self.imagePath = "resources/TreasureChestOpen.png"
		self.set_interactableLootLabel(self.imagePath)



	def active_ogre(self):

		self.imagePath = "resources/OgreAlive.png"
		self.set_interactableEnemyLabel(self.imagePath)

	def dead_ogre(self):

		self.imagePath = "resources/OgreDead.jpg"
		self.set_interactableEnemyLabel(self.imagePath)

	def active_spider(self):

		self.imagePath = "resources/SpiderAlive.jpg"
		self.set_interactableEnemyLabel(self.imagePath)

	def dead_spider(self):

		self.imagePath = "resources/SpiderDead.png"
		self.set_interactableEnemyLabel(self.imagePath)