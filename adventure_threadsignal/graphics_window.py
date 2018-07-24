#!/usr/bin/env python3

from main_window import MainWindow
from PyQt5.QtWidgets import QApplication

def main():
	"""
	The main function, runs when the script is called from the command line

	"""
	# Handler for the event loop
	application = QApplication([])

	# Makes an instance of the MainWindow class
	mainWindow = MainWindow()
	# Calls MainWindow method .show()
	mainWindow.show()

	# .exec begins the while loop for the event loop, does not exit until receives
	# user input
	exit(application.exec())




if (__name__ == '__main__'):
	main()