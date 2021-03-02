import sys
import Window

app2 = Window.QApplication(sys.argv)
Window.QApplication.setApplicationName("U-Dork")
mainwindow = Window.MainWindow()
app2.exec_()