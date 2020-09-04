##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bscontrol
from tologfile import tologfile
from data.books import books
from data.books import bookstores

def main():
    bot = bscontrol()

    print('----------Kosmas----------')
    bot.WebPage(bookstores.iBookstores['Kosmas'])
    iKosmas = bot.KosSearch(books.iBooksKos, books.iRefsKos)
    bot.KosStock(iKosmas)
    

    print('----------Dobrovsky----------')
    bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    iDobrovsky = bot.DobrSearch(books.iBooksDobr)
    # iStock = bot.KosStock(books.iBooks, iTemp)
    iStock = bot.DobrStock(books.iBooksDobr, iDobrovsky)
    bot.PrintBooks(iStock)

    
    print('----------Luxor----------')
    bot.WebPage(bookstores.iBookstores['Luxor'])
    iLuxor = bot.LuxSearch(books.iBooksLux, books.iRefsLux)
    iLuxStock = bot.LuxStock(iLuxor, books.iBooksLux)
    bot.PrintBooks(iLuxStock)


    print('----------Martinus----------')
    bot.WebPage(bookstores.iBookstores['Martinus'])
    iMartinus = bot.MarSearch(books.iBooksMar)
    iMartinus = bot.MarUrl(books.iBooksMarDic, iMartinus)
    iMarStock = bot.MarStock(books.iBooksMar, iMartinus)
    bot.PrintBooks(iMarStock)
    return 0

if __name__ == '__main__':
    # Source code
    main()
