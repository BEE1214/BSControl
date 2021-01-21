##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bscontrol
from tologfile import tologfile
from data.books import books
from interface import terminalinterface

def main():

    interface = terminalinterface()

    interface.MainMenu()
    
    return 0

if __name__ == '__main__':
    # Source code
    main()
