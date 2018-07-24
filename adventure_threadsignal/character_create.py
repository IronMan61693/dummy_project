import sys
import time

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QLineEdit, QComboBox, QFormLayout, QTextEdit
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QImage, QColor

import Game


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

class gameThread (QThread):
	def __init__(self, player_class = "No Class"):

		self.players_class = player_class
		self.playclass = Game.playClass(self.players_class)
		super().__init__()

	def run(self):
		
		while (self.playclass.play()):
			time.sleep(3)


class CharacterCreateWidget(QWidget):
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
	procGame = pyqtSignal(int)
	procCharLabel = pyqtSignal(str)
	procRoomDescription = pyqtSignal(str)
	procRoomAvailableAction = pyqtSignal(list)

	def __init__(self):

		

		self.player_class = "No Class"

		super().__init__()


		######################################################################################################
		# Creating Layouts
		######################################################################################################

		# Sets as child to CentralWidget
		self.mainLayout = QVBoxLayout(self)

		self.nameAndDateLayout = QHBoxLayout()

		self.interactionLayout = QVBoxLayout()

		self.attributeInventoryLayout = QHBoxLayout()

		self.imageInventoryLayout = QVBoxLayout()

		self.attributesLayout = QVBoxLayout()

		# Form layout for class and difficulty setters
		self.comboBoxesFormLayout = QFormLayout()


		######################################################################################################
		# Creating widgets to go in layouts
		######################################################################################################
	
		self.nameLabel = QLabel("Name: ")

		# examples of time and date time
		self.dateTime = QDateTime.currentDateTime()
		self.dateTimeLabel = QLabel(self.dateTime.toString())

		# Changes the name Label
		self.nameLineEdit = QLineEdit("Enter name here ")

		# Character background
		self.characterTextEdit = QTextEdit("Enter your background here")

		# Changes the below labels
		self.classSelectorComboBox = QComboBox()
		self.classSelectorComboBox.addItems(["No Class","Barbarian", "Knight", "Nerd", "Rogue"])

		# Have 3 options that dont do anything
		# Have a tool tip that examples higher difficulties get harder faster
		self.difficultyComboBox = QComboBox()
		self.difficultyComboBox.addItems(["Newb", "Decent", "Gud"])

		self.difficultyLabel = QLabel("A good difficulty for children and casuals")

		# Close the window
		self.finishPushButton = QPushButton("Finish")

		# Change labels with name.setText (to change on classSelecterCombo box changes)
		self.strengthLabel = QLabel("Strength: 10")

		self.dexterityLabel = QLabel("Dexterity: 10")

		self.constitutionLabel = QLabel("Constitution: 10")

		self.intellectLabel = QLabel("Intellect: 10")

		self.smallImageLabel = QLabel()

		self.inventoryLabel = QLabel("No class starts with a fist")



		######################################################################################################
		# Changing the looks of the widgets
		######################################################################################################

		# ~/Documents/py/graphics_Basics/character_select/resources/
		self.imageResourceString = "resources/questionbox.jpg"
		self.smallImage = QImage(self.imageResourceString)
		self.smallerImage= self.smallImage.scaled(50,50)

		self.smallImagePixmap = QPixmap(self.smallerImage)

		self.smallImageLabel.setPixmap(self.smallImagePixmap)


		# Center imageInventory layout
		self.imageInventoryLayout.setAlignment(Qt.AlignCenter)

		## Center the image left to right in the layout
		self.smallImageLabel.setAlignment(Qt.AlignCenter)


		## Changing the colors of finishPushButton, difficultyComboBox, classSelectorComboBox
		newPalettePushButton = self.finishPushButton.palette()
		newPalettePushButton.setColor(newPalettePushButton.Button, QColor(255, 0, 0))
		self.finishPushButton.setAutoFillBackground( True )
		self.finishPushButton.setPalette(newPalettePushButton)

		newPaletteDifficultyComboBox = self.difficultyComboBox.palette()
		newPaletteDifficultyComboBox.setColor(self.difficultyComboBox.backgroundRole(), QColor(123, 123, 123))
		self.difficultyComboBox.setAutoFillBackground( True )
		self.difficultyComboBox.setPalette(newPaletteDifficultyComboBox)






		######################################################################################################
		# re-Parenting mainLayout
		######################################################################################################

		# The order widgets are added change the order they appear in the layout
		# Since main is QV order determines top to bottom
		self.mainLayout.addLayout(self.nameAndDateLayout)

		self.mainLayout.addLayout(self.interactionLayout)

		self.mainLayout.addLayout(self.attributeInventoryLayout)


		######################################################################################################
		# re-Parenting nameAndDateLayout
		######################################################################################################

		# The order widgets are added change the order they appear in the layout
		# Since button is QH order determines left to right
		self.nameAndDateLayout.addWidget(self.nameLabel)

		self.nameAndDateLayout.addWidget(self.dateTimeLabel)


		######################################################################################################
		# re-Parenting interactionLayout
		######################################################################################################

		self.interactionLayout.addWidget(self.nameLineEdit)

		self.interactionLayout.addLayout(self.comboBoxesFormLayout)

		self.interactionLayout.addWidget(self.difficultyLabel)

		self.interactionLayout.addWidget(self.characterTextEdit)

		self.interactionLayout.addWidget(self.finishPushButton)

		######################################################################################################
		# re-Parenting attributeInventoryLayout
		######################################################################################################

		self.attributeInventoryLayout.addLayout(self.attributesLayout)

		self.attributeInventoryLayout.addLayout(self.imageInventoryLayout)


		######################################################################################################
		# re-Parenting attributesLayout
		######################################################################################################

		self.attributesLayout.addWidget(self.strengthLabel)

		self.attributesLayout.addWidget(self.dexterityLabel)

		self.attributesLayout.addWidget(self.constitutionLabel)

		self.attributesLayout.addWidget(self.intellectLabel)

		######################################################################################################
		# re-Parenting imageInventoryLayout
		######################################################################################################

		self.imageInventoryLayout.addWidget(self.smallImageLabel)

		self.imageInventoryLayout.addWidget(self.inventoryLabel)



		######################################################################################################
		# Creating form layout for comboBoxesFormLayout
		######################################################################################################

		self.comboBoxesFormLayout.addRow("Class: ", self.classSelectorComboBox)

		self.comboBoxesFormLayout.addRow("Difficulty: ",self.difficultyComboBox)


		######################################################################################################
		# Connecting the widgets with methods
		######################################################################################################

		self.nameLineEdit.textChanged.connect(self.nameChange)

		self.classSelectorComboBox.activated[str].connect(self.classChange)

		self.classSelectorComboBox.activated[str].connect(self.classImageChange)

		self.difficultyComboBox.activated[str].connect(self.difficultyChange)

		self.finishPushButton.clicked.connect(self.finishChange)


	######################################################################################################
	# On Click Methods
	######################################################################################################



	def classChange(self, classNameText):
		"""
		Edits labels based on classNameText value
		## Create a stack layout and have each class have a VBoxLayout and when the signal is sent I change the image that is on top

		Input:
			classNameText <str>

		Output: None
		"""
		if (classNameText == "Barbarian"):

			self.strengthLabel.setText("Strength: 14")

			self.dexterityLabel.setText("Dexterity: 8")

			self.constitutionLabel.setText("Constitution: 12")

			self.intellectLabel.setText("Intellect: 6")

			self.inventoryLabel.setText("Barbarians start with an axe")



		elif (classNameText == "Knight"):

			self.strengthLabel.setText("Strength: 12")

			self.dexterityLabel.setText("Dexterity: 8")

			self.constitutionLabel.setText("Constitution: 12")

			self.intellectLabel.setText("Intellect: 8")

			self.inventoryLabel.setText("Knight = Sword, Duh")

		elif (classNameText == "Nerd"):

			self.strengthLabel.setText("Strength: 8")

			self.dexterityLabel.setText("Dexterity: 8")

			self.constitutionLabel.setText("Constitution: 8")

			self.intellectLabel.setText("Intellect: 16")

			self.inventoryLabel.setText("Nerds have no weapons")

		elif (classNameText == "Rogue"):

			self.strengthLabel.setText("Strength: 6")

			self.dexterityLabel.setText("Dexterity: 14")

			self.constitutionLabel.setText("Constitution: 8")

			self.intellectLabel.setText("Intellect: 12")

			self.inventoryLabel.setText("Rogues get a dagger")

		elif (classNameText == "No Class"):

			self.strengthLabel.setText("Strength: 10")

			self.dexterityLabel.setText("Dexterity: 10")

			self.constitutionLabel.setText("Constitution: 10")

			self.intellectLabel.setText("Intellect: 10")

			self.inventoryLabel.setText("No class starts with a fist")

		self.player_class = classNameText



	def classImageChange(self, classNameText):
		"""
		Edits labels based on classNameText value

		Input:
			classNameText <str>

		Output: None
		"""
		

		if (classNameText == "Barbarian"):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/barbarian.jpg"
			self.smallImage = QImage(self.imageResourceString)
			self.smallerImage= self.smallImage.scaled(50,50)

			self.smallImagePixmap = QPixmap(self.smallerImage)

			self.smallImageLabel.setPixmap(self.smallImagePixmap)

		elif (classNameText == "Knight"):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/knight.jpg"
			self.smallImage = QImage(self.imageResourceString)
			self.smallerImage= self.smallImage.scaled(50,50)

			self.smallImagePixmap = QPixmap(self.smallerImage)

			self.smallImageLabel.setPixmap(self.smallImagePixmap)

		elif (classNameText == "Nerd"):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/questionbox.jpg"
			self.smallImage = QImage(self.imageResourceString)
			self.smallerImage= self.smallImage.scaled(50,50)

			self.smallImagePixmap = QPixmap(self.smallerImage)

			self.smallImageLabel.setPixmap(self.smallImagePixmap)

		elif (classNameText == "Rogue"):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/rogue.png"
			self.smallImage = QImage(self.imageResourceString)
			self.smallerImage= self.smallImage.scaled(50,50)

			self.smallImagePixmap = QPixmap(self.smallerImage)

			self.smallImageLabel.setPixmap(self.smallImagePixmap)

		elif (classNameText == "No Class"):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/questionbox.jpg"
			self.smallImage = QImage(self.imageResourceString)
			self.smallerImage= self.smallImage.scaled(50,50)

			self.smallImagePixmap = QPixmap(self.smallerImage)

			self.smallImageLabel.setPixmap(self.smallImagePixmap)



	def difficultyChange(self, difficultyText):
		"""
		Edits labels based on difficultyText value

		Input:
			difficultyText <str>

		Output: None
		"""

		if (difficultyText == "Newb"):

			self.difficultyLabel.setText("A good difficulty for children and casuals")

		elif (difficultyText == "Decent"):

			self.difficultyLabel.setText("Fun and exciting adventure awaits")


		elif (difficultyText == "Gud"):

			self.difficultyLabel.setText("Good luck")

	def finishChange(self):
		"""
		TBD sends information decided on in the screen to game state
		Currently exits

		Input: None
			
		Output: None
		"""
		self.game_thread = gameThread(self.player_class)
		self.game_thread.start()
		self.procGame.emit(1)
		self.procCharLabel.emit(self.imageResourceString)
		self.procRoomDescription.emit(self.game_thread.playclass.getTileDescription())
		self.procRoomAvailableAction.emit(self.game_thread.playclass.getAvailableActions())




	def nameChange(self, nameText):
		"""
		Changes nameLabel

		Input:
			nameText <str>

		Output: None
		"""
		self.nameLabel.setText("Name: " + nameText)



	def userInputChange(self, userInput):
		self.game_thread.playclass.setUserAction(userInput)

		
		self.procCharLabel.emit(self.imageResourceString)
		self.procRoomDescription.emit(self.game_thread.playclass.getTileDescription())
		self.procRoomAvailableAction.emit(self.game_thread.playclass.getAvailableActions())