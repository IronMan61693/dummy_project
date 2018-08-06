from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor

from central_widget import CentralWidget

class MainWindow(QMainWindow):
	"""
	We are modifying some of the attributes of a QMainWindow class
	Create an instance of CentralWidget class
	
	Variables:
		centralWidget <CentralWidget>
		newPalette <QPalette> is used to change the main background color of the widget
		mainMenuBar <menuBar>
		fileMenu <menu>
		characterMenu <menu>
		helpMenu <menu>
		uploadAction <QAction>
		exitAction <QAction>
		characterAction <QAction>
		inventoryAction <QAction>
		equipmentAction <QAction>
		roomDescAction <QAction>
		actionAvailAction <QAction>
		characterStuckAction <QAction>
		helpMeAction <QAction>



	Methods:
		Inherited from QMainWindow:
			setCentralWidget 
			setPalette 
			setWindowTitle
			addMenu
			addAction

		showMenuBar used to change the visibility of the menu bar
	"""
	def __init__(self):
		super().__init__()

		######################################################################################################
		# Change settings for central widget
		######################################################################################################

		self.centralWidget = CentralWidget()
	
		newPalette = self.centralWidget.palette()
		newPalette.setColor(self.centralWidget.backgroundRole(), QColor(0, 105, 105))
		self.centralWidget.setAutoFillBackground( True )
		self.centralWidget.setPalette(newPalette)

		
		self.centralWidget.setFixedWidth(580)
		self.centralWidget.setFixedHeight(600)

		self.setCentralWidget(self.centralWidget)

		self.setWindowTitle("The Game")

		######################################################################################################
		# Create menu bar
		######################################################################################################


		self.mainMenuBar = self.menuBar()

		fileMenu = self.mainMenuBar.addMenu('File')
		characterMenu = self.mainMenuBar.addMenu('Character')
		helpMenu = self.mainMenuBar.addMenu('Help')

		######################################################################################################
		# Create and set actions
		######################################################################################################

		uploadAction = QAction('Upload Game To Website', self)
		uploadAction.triggered.connect(self.centralWidget.uploadGameInfo)
		exitAction = QAction('Exit', self)
		exitAction.triggered.connect(qApp.quit)

		characterAction = QAction('Character Info', self)
		characterAction.triggered.connect(self.centralWidget.showCharacterInfo)
		inventoryAction = QAction('Inventory', self)
		inventoryAction.triggered.connect(self.centralWidget.showInventoryInfo)
		equipmentAction = QAction('Equipment', self)
		equipmentAction.triggered.connect(self.centralWidget.changeEquipmentGeneral)

		roomDescAction = QAction('Description', self)
		roomDescAction.triggered.connect(self.centralWidget.showRoomDesc)
		actionAvailAction = QAction('Actions', self)
		actionAvailAction.triggered.connect(self.centralWidget.showAvailActions)
		characterStuckAction = QAction('Stuck? Click here', self)
		characterStuckAction.triggered.connect(self.centralWidget.unstuckCharacter)
		helpMeAction = QAction('Helpful Info', self)
		helpMeAction.triggered.connect(self.centralWidget.showHelpfulInfo)

		######################################################################################################
		# Pair actions with menubar
		######################################################################################################

		fileMenu.addAction(uploadAction)
		fileMenu.addAction(exitAction)

		characterMenu.addAction(characterAction)
		characterMenu.addAction(inventoryAction)
		characterMenu.addAction(equipmentAction)

		helpMenu.addAction(roomDescAction)
		helpMenu.addAction(actionAvailAction)
		helpMenu.addAction(characterStuckAction)
		helpMenu.addAction(helpMeAction)

		######################################################################################################
		# Show menu visibility
		######################################################################################################

		self.mainMenuBar.setVisible(False)
		self.centralWidget.procShowMenu.connect(self.showMenuBar)

	def showMenuBar(self):
		self.mainMenuBar.setVisible(True)







		