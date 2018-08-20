import sys
import time

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QLineEdit, QComboBox, QFormLayout, QTextEdit
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QImage, QColor




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

class CharacterCreateWidget(QWidget):
	"""
	Making a class from the QWidget class, is used in the game to receive information
	 from the user to be used for the character's information.

	Variables:
		mainLayout <QVBoxLayout>
		interactionLayout <QVBoxLayout>
		attributeInventoryLayout <QHBoxLayout>
		attributeLayout <QVBoxLayout>
		informationFormLayout<QFormLayout>

		characterNameLineEdit <QLineEdit>
		playerNameLineEdit <QLineEdit>
		classSelectorComboBox <QComboBox>
		difficultyComboBox <QComboBox>
		finishPushButton <QPushButton>

		difficultyLabel <QLabel>
		strengthLabel <QLabel>
		dexterifyLabel <QLabel>
		constitutionLabel <QLabel>
		intellectLabel <QLabel>
		smallImageLabel <QLabel>
		inventoryLabel <QLabel>

		

		player_class <str>
		player_name <str>
		character_name <str>
		barbarianString <str>
		noClassString <str>
		knightString <str>
		nerdString <str>
		rogueString <str>
		imageResourceString <str>

	Methods:
		classChange Changes text labels related to class
		classImageChange Changes image related to class
		difficultyChange Changes difficulty label
		finishChange Emits signals to centralwidget with the information provided by this screen
		playerNameChange Changes player_name variables 
		
	"""
	procGameStart = pyqtSignal(int, str, str, str)
	procCharLabel = pyqtSignal(str)

	def __init__(self):

		

		self.player_class = "No Class"
		self.player_name = "Zorg"
		self.character_name = "Character"

		self.barbarianString = "Barbarian"
		self.noClassString = "No Class"
		self.knightString = "Knight"
		self.nerdString = "Nerd"
		self.rogueString = "Rogue"


		super().__init__()


		######################################################################################################
		# Creating Layouts
		######################################################################################################

		# Sets as child to CentralWidget
		self.mainLayout = QVBoxLayout(self)

		self.interactionLayout = QVBoxLayout()

		self.attributeInventoryLayout = QHBoxLayout()

		self.imageInventoryLayout = QVBoxLayout()

		self.attributesLayout = QVBoxLayout()

		# Form layout for class and difficulty setters
		self.informationFormLayout = QFormLayout()
		self.informationFormLayout.setVerticalSpacing(25)


		######################################################################################################
		# Creating widgets to go in layouts
		######################################################################################################

		# Used to enter the player's name
		self.playerNameLineEdit = QLineEdit()
		self.playerNameLineEdit.setPlaceholderText("Enter player name here ")

		# Used to enter the character's name
		self.characterNameLineEdit = QLineEdit()
		self.characterNameLineEdit.setPlaceholderText("Enter character name here ")

		# Changes the below labels
		self.classSelectorComboBox = QComboBox()
		self.classSelectorComboBox.addItems([self.noClassString,self.barbarianString, self.knightString, self.nerdString, self.rogueString])

		# TBD add difficulty to game
		self.difficultyComboBox = QComboBox()
		self.difficultyComboBox.addItems(["Newb", "Decent", "Gud"])

		# Used to start the game
		self.finishPushButton = QPushButton("Finish")


		# Labels to display information to the user
		self.difficultyLabel = QLabel("A good difficulty for children and casuals")

		self.strengthLabel = QLabel("Strength: 10")

		self.dexterityLabel = QLabel("Dexterity: 10")

		self.constitutionLabel = QLabel("Constitution: 10")

		self.intellectLabel = QLabel("Intellect: 10")

		self.smallImageLabel = QLabel()

		self.inventoryLabel = QLabel("Ever class starts with a fist and shredded rags")



		######################################################################################################
		# Changing the looks of the widgets
		######################################################################################################

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
		self.mainLayout.addLayout(self.interactionLayout)

		self.mainLayout.addLayout(self.attributeInventoryLayout)

		self.mainLayout.addWidget(self.finishPushButton)


		######################################################################################################
		# re-Parenting interactionLayout
		######################################################################################################

		self.interactionLayout.addLayout(self.informationFormLayout)

		self.interactionLayout.addWidget(self.difficultyLabel)


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
		# Creating form layout for informationFormLayout
		######################################################################################################

		self.informationFormLayout.addRow("Player Name: ", self.playerNameLineEdit)

		self.informationFormLayout.addRow("Character Name: ", self.characterNameLineEdit)

		self.informationFormLayout.addRow("Class: ", self.classSelectorComboBox)

		self.informationFormLayout.addRow("Difficulty: ", self.difficultyComboBox)


		######################################################################################################
		# Connecting the widgets with methods
		######################################################################################################

		self.playerNameLineEdit.textChanged.connect(self.playerNameChange)

		self.characterNameLineEdit.textChanged.connect(self.characterNameChange)

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

		Output: 
			Change labels
		"""
		self.strengthString = "Strength: 10"
		self.dexterityString = "Dexterity: 10"
		self.constitutionString = "Constitution: 10"
		self.intellectString = "Intellect: 10"
		self.inventoryString = "No class starts with a fist"

		if (classNameText == self.barbarianString):

			self.strengthString ="Strength: 14"

			self.dexterityString = "Dexterity: 8"

			self.constitutionString = "Constitution: 12"

			self.intellectString = "Intellect: 6"

			self.inventoryString = "Barbarians start with an axe"



		elif (classNameText == self.knightString):

			self.strengthString = "Strength: 12"

			self.dexterityString = "Dexterity: 8"

			self.constitutionString = "Constitution: 12"

			self.intellectString = "Intellect: 8"

			self.inventoryString = "Knight = Sword, Duh"

		elif (classNameText == self.nerdString):

			self.strengthString = "Strength: 8"

			self.dexterityString = "Dexterity: 8"

			self.constitutionString = "Constitution: 8"

			self.intellectString = "Intellect: 16"

			self.inventoryString = "Nerds have no weapons"

		elif (classNameText == self.rogueString):

			self.strengthString = "Strength: 6"

			self.dexterityString = "Dexterity: 14"

			self.constitutionString = "Constitution: 8"

			self.intellectString = "Intellect: 12"

			self.inventoryString = "Rogues get a dagger"

		
		self.player_class = classNameText

		self.strengthLabel.setText(self.strengthString)

		self.dexterityLabel.setText(self.dexterityString)

		self.constitutionLabel.setText(self.constitutionString)

		self.intellectLabel.setText(self.intellectString)

		self.inventoryLabel.setText(self.inventoryString)




	def classImageChange(self, classNameText):
		"""
		Edits labels based on classNameText value

		Input:
			classNameText <str>

		Output: None
		"""
		

		if (classNameText == self.barbarianString):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/barbarian.jpg"
			

		elif (classNameText == self.knightString):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/knight.jpg"
			

		elif (classNameText == self.nerdString):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/nerd.jpg"
			

		elif (classNameText == self.rogueString):

			# ~/Documents/py/graphics_Basics/character_select/resources/
			self.imageResourceString = "resources/rogue.png"
			

		elif (classNameText == self.noClassString):

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
		
		self.procGameStart.emit(1, self.player_class, self.character_name, self.player_name)
		self.procCharLabel.emit(self.imageResourceString)
		




	def playerNameChange(self, nameText):
		"""
		Changes player_name variable

		Input:
			nameText <str>

		Output: None
		"""
		self.player_name = nameText



	def characterNameChange(self, nameText):
		"""
		Changes character_name variable

		Input:
			nameText <str>

		Output: None
		"""
		self.character_name = nameText


