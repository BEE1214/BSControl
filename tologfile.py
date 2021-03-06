##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-19 -=##
##=================================##
from datetime import datetime
from sys import exc_info
from enum import Enum

# from errors import errors

class errors(Enum):
    OK = 0
    CannotOpen = 1
    CannotWrite = 2

class tologfile:
    """Library with functions to log into files Search.txt and Stock.txt.
    """
    iCount = 0

    def __init__(self, aFile):
        self.iFile = aFile
        try:
            if (tologfile.iCount < 2):
                self.iLogFile = open(self.iFile, 'w')
            else:
                self.iLogFile = open(self.iFile, 'a')
        except:
            print(f'{exc_info()[0]}')
        tologfile.iCount += 1
    
    def tofile(self, aList):
        """Print list to specified text file in class variable iFile.

        Args:
            aList (list): List to print into the text file

        Returns:
            enum: errors from class errors
                  posible options: OK/CannotWrite
        """
        try:
            # self.iLogFile.write(datetime.now().strftime("%Y-%m-%d - %H:%M"))
            self.iLogFile.write('/=======================================================================\\')
            self.iLogFile.write(" \n")
            for i in range(len(aList)):
                self.iLogFile.write(aList[i])
                self.iLogFile.write('\n')
        except:
            print(f'{exc_info()[0]}')
            return errors.CannotWrite
        return errors.OK