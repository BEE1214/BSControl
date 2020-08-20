##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-19 -=##
##=================================##

class tologfile:

    def __init__(self, aStockBooks):
        self.iStockBooks = aStockBooks
        pass

    def tofile(self):
        iBooksLog = open('booklog.txt', 'w+')
        for i in range(len(self.iStockBooks)):
            iBooksLog.write(self.iStockBooks[i])
        pass
    pass