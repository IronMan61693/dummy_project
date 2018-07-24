

from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtCore import pyqtSignal

from character_create import CharacterCreateWidget
from base_graphic_worldtile import BaseGraphicWorldTileWidget
from Game import playClass



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
	def __init__(self):

		super().__init__()

		self.Stack = QStackedWidget(self)
		self.characterCreateWidget = CharacterCreateWidget()
		self.baseGraphicWorldTileWidget = BaseGraphicWorldTileWidget()

		self.characterCreateWidget.procGameStart.connect(self.start_game)
		self.characterCreateWidget.procCharLabel.connect(self.baseGraphicWorldTileWidget.set_player_image)
		


		self.Stack.addWidget (self.characterCreateWidget)
		self.Stack.addWidget (self.baseGraphicWorldTileWidget)





	def start_game(self, index, character_class_name):
		self.Stack.setCurrentIndex(index)
		self.game = playClass(character_class_name)
		self.editInteractableTile()
		


	



	def keyPressEvent (self, event):
		super().keyPressEvent
		# self.editGraphicTile()
		self.userInputAction(event.text())
		self.game.doAction()
		self.editInteractableTile()
		


	def userInputAction(self, actionString):

		self.game.setUserAction(actionString)



	def editInteractableTile(self):
		self.game.enterRoom()
		self.tileDescription = self.game.getTileDescription()
		self.actionDescription = self.game.getAvailableActions()
		self.baseGraphicWorldTileWidget.set_room_description(self.tileDescription)
		self.baseGraphicWorldTileWidget.set_actions(self.actionDescription)

		self.roomType = self.game.getTypeOfRoom()
		# Return 0 if not loot room
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

		
