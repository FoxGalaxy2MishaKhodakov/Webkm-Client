from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://webkm.ru/"))

        self.setCentralWidget(self.browser)

        self.show()

app = QApplication(sys.argv)
app.setApplicationName("WebKM")
app.setWindowIcon(QtGui.QIcon('icon.png'))
window = MainWindow()

app.exec_()
