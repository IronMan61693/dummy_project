from PyQt5.QtWidgets import QMainWindow
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
		newPalette.setColor(self.centralWidget.backgroundRole(), QColor(105, 105, 105))
		self.centralWidget.setAutoFillBackground( True )
		self.centralWidget.setPalette(newPalette)


		self.centralWidget.setFixedWidth(325)
		self.centralWidget.setFixedHeight(500)

		self.setCentralWidget(self.centralWidget)

		self.setWindowTitle("The Game")




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

		
