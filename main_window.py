##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2021-02-10 -=##
##=================================##

import PyQt5.QtWidgets as qtw
from window_pyqt import Ui_MainWindow as qtmain


class Ui_Window(qtmain):
    def __init__(self):
        super(Ui_Window,self).__init__()
        

    #     self.show()
    
    def check(self):
        self.check_Dobrovsky.toggled.connect()
    pass
