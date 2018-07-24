

from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtCore import pyqtSignal

from character_create import CharacterCreateWidget
from base_graphic_worldtile import BaseGraphicWorldTileWidget



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

		self.characterCreateWidget.procGame.connect(self.change_index)
		self.characterCreateWidget.procCharLabel.connect(self.baseGraphicWorldTileWidget.set_player_image)
		self.characterCreateWidget.procRoomDescription.connect(self.baseGraphicWorldTileWidget.set_room_description)
		self.characterCreateWidget.procRoomAvailableAction.connect(self.baseGraphicWorldTileWidget.set_actions)
		self.baseGraphicWorldTileWidget.procGameChange.connect(self.characterCreateWidget.userInputChange)

		self.Stack.addWidget (self.characterCreateWidget)
		self.Stack.addWidget (self.baseGraphicWorldTileWidget)





	def change_index(self, index):
		self.Stack.setCurrentIndex(index)
		

