from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Dork_Window(QWidget):

	def __init__(self):
		super().__init__()
		self.layout = QFormLayout()
		self.setWindowTitle("Dorks")
		self.setLayout(self.layout)
		self.createIndividualCommands()
		self.layoutButtons()

	# Creates the dork commands needed for each line by adding the text box and formatting.
	def dorkCommandCreation(self, commandOfDork):
		self.commandOfDork = commandOfDork
		self.dork = QLineEdit()
		self.dork.setFont(QFont("Arial", 20))
		self.layout.addRow(self.commandOfDork, self.dork)

	# Loops through an Array and creates each line of the dork words.
	def createIndividualCommands(self):
		dorkCommandNames = ["intitle:", "inurl:", "filetype:", "ext:", "intext:", "site:", "Cache:", "*     :"]
		for i in dorkCommandNames:
			self.dorkCommandCreation(i)

	#Creates the buttons for the layout
	def layoutButtons(self):
		self.confirmButton = QPushButton("Confirm", self)
		self.cancelButton = QPushButton("Cancel", self)
		self.layout.addWidget(self.confirmButton)
		self.layout.addWidget(self.cancelButton)
		self.confirmButton.setFixedWidth(188)
		self.cancelButton.setFixedWidth(188)

