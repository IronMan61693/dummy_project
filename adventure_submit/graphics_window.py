#!/usr/bin/env python3

from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QProcess, QCoreApplication


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

	# A process for handling the web method, it is an infinite loop so needs to be handled 
	# in a seperate process
	webProcess = QProcess()

	# 127.0.0.1:5000 the current host 
	webProcess.start("python3 WebRun.py")

	# .exec begins the while loop for the event loop, does not exit until receives
	# user input
	application.exec()
	webProcess.terminate()
	exit()




if (__name__ == '__main__'):
	main()

