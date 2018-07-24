from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage, QKeyEvent

from character_create import CharacterCreateWidget




class BaseGraphicWorldTileWidget (QWidget):

	procGameChange = pyqtSignal(str)

	def __init__(self):
		super().__init__()

		self.mainLayout = QVBoxLayout(self)
	
		self.gameBorderFrame = QFrame()
		self.gameBorderFrame.setStyleSheet("background-color: rgb(147,145,150)")
		self.gameBorderFrame.setMinimumWidth(305)
		self.gameBorderFrame.setMinimumHeight(460)

		self.mainInnerLayout = QVBoxLayout(self.gameBorderFrame)
		self.topInnerLayout = QVBoxLayout()
		self.middleInnerLayout = QHBoxLayout()
		self.bottomInnerLayout = QVBoxLayout()

		self.holdCharacterInteractionLayout = QVBoxLayout()
	
		
		self.roomDescriptionLabel = QLabel()
		self.roomDescriptionLabel.setText("This is where the description of the current mapTile will go")
		self.roomDescriptionLabel.setWordWrap( True )

		self.actionsLabel = QLabel()
		self.actionsLabel.setText("This is where actions go")
		self.actionsLabel.setWordWrap( True )

		self.playerLabel = QLabel()
		self.playerLabel.setText("Player")

		self.interactableLabel = QLabel()
		self.interactableLabel.setText("Interaction")
		self.interactableLabel.hide()

		self.topDoorLabel = QLabel()
		self.leftDoorLabel = QLabel()
		self.rightDoorLabel = QLabel()
		self.bottomDoorLabel = QLabel()

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
		self.roomDescriptionLabel.setAlignment(Qt.AlignCenter)
		self.actionsLabel.setAlignment(Qt.AlignCenter)




		self.mainInnerLayout.addStretch(0)
		self.mainInnerLayout.addLayout(self.topInnerLayout)
		self.mainInnerLayout.addStretch(9)
		self.mainInnerLayout.addLayout(self.middleInnerLayout)
		self.mainInnerLayout.addStretch(1)
		self.mainInnerLayout.addWidget(self.roomDescriptionLabel)
		self.mainInnerLayout.addStretch(0)
		self.mainInnerLayout.addWidget(self.actionsLabel)
		self.mainInnerLayout.addStretch(0)
		self.mainInnerLayout.addLayout(self.bottomInnerLayout)


		self.topInnerLayout.addWidget(self.topDoorLabel)
		self.topInnerLayout.addWidget(self.interactableLabel)

		self.middleInnerLayout.addWidget(self.leftDoorLabel)
		self.middleInnerLayout.addLayout(self.holdCharacterInteractionLayout)
		self.middleInnerLayout.addWidget(self.rightDoorLabel)

		self.bottomInnerLayout.addWidget(self.bottomDoorLabel)	


		self.holdCharacterInteractionLayout.addWidget(self.interactableLabel)
		self.holdCharacterInteractionLayout.addStretch(1)
		self.holdCharacterInteractionLayout.addWidget(self.playerLabel)



		self.mainLayout.addWidget(self.gameBorderFrame)

	

	def set_player_image(self, resourcePath):
		self.playerImage = QImage(resourcePath)
		self.playerImage = self.playerImage.scaled(50,50)

		self.playerPixmap = QPixmap(self.playerImage)

		self.playerLabel.setPixmap(self.playerPixmap)

	def set_room_description(self, roomDescription):
		self.roomDescriptionLabel.setText(roomDescription)

	def set_actions(self, actions):
		actionString = "Actions:\n"
		for action in actions:
			actionString = actionString + str(action) + "       "
		self.actionsLabel.setText(actionString)

	def keyPressEvent (self, event):
		super().keyPressEvent
		self.procGameChange.emit(event.text())