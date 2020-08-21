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
    bot.WebPage(bookstores.iBookstores['Kosmas'])
    # bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    iTemp = bot.KosSearch(books.iBooks, books.iRefs)
    print(iTemp)
    # iTemp = bot.DobrSearch(books.iBooks, books.iRefs)
    # iStock = bot.KosStock(books.iBooks, iTemp)
    # iStock = bot.DobrStock(books.iBooks, iTemp)
    # for i in range(len(iStock)):
    #     if(iStock[i].find('neni skladem'))
    #         print(iStock[i])
    #     pass

if __name__ == '__main__':
    # Source code
    main()