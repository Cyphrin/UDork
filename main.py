import sys
import Origin_Window

app2 = Origin_Window.QApplication(sys.argv)
Origin_Window.QApplication.setApplicationName("U-Dork")
mainwindow = Origin_Window.MainWindow()
app2.exec_()