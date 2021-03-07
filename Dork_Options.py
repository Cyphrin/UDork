from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Dork_Window():


	def window(self):
		self.flo = QFormLayout()
		self.app = QApplication(sys.argv)
		self.win = QWidget()
		self.createIndividualCommands()
		self.setWindow()

	def dorkCommandCreation(self, commandOfDork):

		self.commandOfDork = commandOfDork
		print(self.commandOfDork)
		self.dork = QLineEdit()
		self.dork.setFont(QFont("Arial", 20))
		self.flo.addRow(self.commandOfDork, self.dork)

	# Creates the Individual dork commands
	def createIndividualCommands(self):
		dorkCommandNames = ["intitle:", "inurl:", "filetype:", "ext:", "intext:", "site:", "Cache:", "*:"]
		for i in dorkCommandNames:
			self.dorkCommandCreation(i)

	# Creates the layout and name of the window
	def setWindow(self):
		self.win.setLayout(self.flo)
		self.win.setWindowTitle("Dorks")
		self.win.show()
		sys.exit(self.app.exec_())



# This is to test the line to see if window opens. ###DELETE###
if __name__ == '__main__':
	a = Dork_Window()
	a.window()
