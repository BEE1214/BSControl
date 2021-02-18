##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bscontrol
from tologfile import tologfile
from data.books import books
from interface import terminalinterface
from PyQt5 import QtWidgets, QtGui, QtCore
from window_pyqt import Ui_MainWindow
import sys
from main_window import Ui_Window

def main():

    interface = terminalinterface()

    interface.MainMenu()

    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    
    return 0

if __name__ == '__main__':
    # Source code
    main()
