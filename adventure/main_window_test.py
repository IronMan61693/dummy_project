from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QColor

from central_widget import CentralWidget

class MainWindow(QMainWindow):
	"""
	We are modifying some of the attributes of a QMainWindow class
	Create an instance of CentralWidget class
	
	Variables:
		centralWidget <CentralWidget>

	Methods:
		Inherited from QMainWindow:
			setCentralWidget 
			setWindowTitle
	"""
	def __init__(self):
		super().__init__()
		self.centralWidget = CentralWidget()
	
		newPalette = self.centralWidget.palette()
		newPalette.setColor(self.centralWidget.backgroundRole(), QColor(0, 105, 105))
		self.centralWidget.setAutoFillBackground( True )
		self.centralWidget.setPalette(newPalette)

		
		self.centralWidget.setFixedWidth(355)
		self.centralWidget.setFixedHeight(580)
		# self.setGeometry(self.left, self.top, self.width, self.height)

		self.setCentralWidget(self.centralWidget)

		self.setWindowTitle("The Game")


		self.mainMenuBar = self.menuBar()

		fileMenu = self.mainMenuBar.addMenu('File')
		characterMenu = self.mainMenuBar.addMenu('Character')
		helpMenu = self.mainMenuBar.addMenu('Help')


		saveAction = QAction('Save', self)
		exitAction = QAction('Exit', self)
		exitAction.triggered.connect(qApp.quit)

		characterAction = QAction('Character Info', self)
		inventoryAction = QAction('Inventory', self)

		roomDescAction = QAction('Description', self)
		actionAvailAction = QAction('Actions', self)


		fileMenu.addAction(saveAction)
		fileMenu.addAction(exitAction)

		characterMenu.addAction(characterAction)
		characterMenu.addAction(inventoryAction)

		helpMenu.addAction(roomDescAction)
		helpMenu.addAction(actionAvailAction)

		self.mainMenuBar.setVisible(False)
		self.centralWidget.procShowMenu.connect(self.showMenuBar)

	def showMenuBar(self):
		self.mainMenuBar.setVisible(True)







		"""
		#Using an image

		# Set the background as a Pixmap /home/dopo2697/Documents/py/graphics_Basics/character_select/resources/burning_guy_background.jpeg
		self.backgroundPixmap = QPixmap("burning_guy_background.jpeg")

		# Create the background Palette and set its background to the Pixmap
		self.backgroundPalette = QPalette()

		self.backgroundBrush = QBrush()
		self.backgroundBrush.setTexture(self.backgroundPixmap)

		# Good colors http://encycolorpedia.com/a2a565

		self.backgroundPalette.setBrush(QPalette.Background, self.backgroundBrush)

		self.centralWidget.setAutoFillBackground( True )

		# change the Palette for the widget
		self.centralWidget.setPalette(self.backgroundPalette)


		self.centralWidget.setObjectName("centralWidget")
		self.centralWidget.setStyleSheet("background-color: blue ; color : #f8f8f8")

		# Create the background Palette and set its background to the Pixmap
		self.backgroundPalette = QPalette()

		

		# Good colors http://encycolorpedia.com/a2a565

		self.backgroundPalette.setColor(self.Background(), QColor(181,166,66))
		self.centralWidget.setAutoFillBackground( True )

		# change the Palette for the widget
		self.centralWidget.setPalette( self.backgroundPalette)



		self.centralWidget.setStyleSheet("background-color: #858585")
		"""

		
