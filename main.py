##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bscontrol
from tologfile import tologfile
from data.books import books
from interface import terminalinterface
import PyQt5.QtWidgets as qtw
from main_window import Ui_Window

def main():

    # interface = terminalinterface()

    # interface.MainMenu()
    
    App = qtw.QApplication([])
    MainW = Ui_Window()
    # MainW.show()
    App.setStyle(qtw.QStyleFactory.create('Fusion'))
    App.exec_()
    return 0

if __name__ == '__main__':
    # Source code
    main()
