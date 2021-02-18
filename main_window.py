##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2021-02-10 -=##
##=================================##

import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore, QtGui

from window_pyqt import Ui_MainWindow


class Ui_Window(qtw.QWidget):
    def __init__(self):
        super(Ui_Window,self).__init__()
        self.app = qtw.QApplication([])
        self.app.setStyle(qtw.QStyleFactory.create('Fusion'))
        self.MainWindow = qtw.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    
    def __del__(self):
        self.exit(self.app.exec_())

        
        

    #     self.show()
    
    def check(self):
        self.check_Dobrovsky.toggled.connect()
    pass
