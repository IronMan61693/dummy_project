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

	webProcess = QProcess()
	webProcess.start("python3 WebRun.py")

	# .exec begins the while loop for the event loop, does not exit until receives
	# user input
	# exit(application.exec())
	application.exec()
	webProcess.terminate()
	exit()




if (__name__ == '__main__'):
	main()



"""
processes = set([])

def finished():
	QCoreApplication.instance().quit()

def launch_web():
	# 127.0.0.1:5000
	webProcess = QProcess()
	processes.add(webProcess)
	webProcess.start("./WebRun.py")
	# webProcess.finished.connect(finished)
	# webProcess.terminate()
	# webProcess.close()
"""