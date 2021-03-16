from Dork_Options import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://google.com'))
		self.setCentralWidget(self.browser)
		self.left = 10
		self.top = 10
		self.width = 1240
		self.height = 1080
		self.initUI()
		self.navbar = QToolBar()
		self.addToolBar(self.navbar)
		self.createNavBarButton()

	def initUI(self):
		# Window Size
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.show()
		self.dorkOpt = Dork_Window()

	def navBarButtonTemplate(self, btnWord, functionOfButton):
		self.btnWord = btnWord
		nav_btn = QAction(btnWord, self)
		nav_btn.triggered.connect(functionOfButton)
		self.navbar.addAction(nav_btn)

	def createNavBarButton(self):
		navbarWords = {
			"Back": self.browser.back,
			"Forward": self.browser.forward,
			"Reload": self.browser.reload,
			"Home": self.navigate_home,
			"Dork": self.dorkOpt.show,
			"Exploit DB": self.navigate_exploitDB
		}
		for x, y in navbarWords.items():
			self.navBarButtonTemplate(x, y)
		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		self.navbar.addWidget(self.url_bar)
		self.browser.urlChanged.connect(self.update_url)

	def navigate_home(self):
		self.browser.setUrl(QUrl('https://www.google.com/'))

	def navigate_exploitDB(self):
		self.browser.setUrl(QUrl('https://www.exploit-db.com/'))

	def navigate_to_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))

	def update_url(self, q):
		self.url_bar.setText(q.toString())
