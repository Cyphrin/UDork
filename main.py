import sys
import OriginWindow

app2 = OriginWindow.QApplication(sys.argv)
OriginWindow.QApplication.setApplicationName("U-Dork")
mainwindow = OriginWindow.MainWindow()
app2.exec_()