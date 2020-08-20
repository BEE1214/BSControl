##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bscontrol
from tologfile import tologfile
from data.books import books
from data.bookstores import bookstores

def main():
    iTemp = []
    bot = bscontrol()
    bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    iTemp = bot.BookSearch(books.iBooks, books.iRefs)
    print(iTemp)
    # iStockBooks = bot.BookCount(books.iBooks, books.iRefs)
    # tofile = tologfile(iStockBooks)
    # tofile.tofile()

if __name__ == '__main__':
    # Source code
    main()