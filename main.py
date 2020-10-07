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

    # print('---------- Kosmas ----------')
    # iKosSearch = bot.BookSearch(books.UrlKos, books.PathKos)
    # iKosStock = bot.BookStock(iKosSearch, books.StockKos)
    # bot.PrintBooks(iKosStock)

    print('---------- Dobrovsky ----------')
    iDobrovskySearch = bot.BookSearch(books.UrlDobr, books.PathDobr)
    iDobrStock = bot.BookStock(iDobrovskySearch, books.StockDobr)
    bot.PrintBooks(iDobrStock)
    # bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    # iDobrovsky = bot.DobrSearch(books.iBooksDobr)
    # # iStock = bot.KosStock(books.iBooks, iTemp)
    # iStock = bot.DobrStock(books.iBooksDobr, iDobrovsky)
    # if(iStock == []) :
    #     print('Vsechny knihy skladem')
    # else :
    #     bot.PrintBooks(iStock)

    
    # print('---------- Luxor ----------')
    # bot.WebPage(bookstores.iBookstores['Luxor'])
    # iLuxor = bot.LuxSearch(books.iBooksLux, books.iRefsLux)
    # iLuxStock = bot.LuxStock(iLuxor, books.iBooksLux)
    # if (iLuxStock == []):
    #     print('Vsechny knihy skladem')
    # else :
    #     bot.PrintBooks(iLuxStock)


    # print('---------- Martinus ----------')
    # bot.WebPage(bookstores.iBookstores['Martinus'])
    # iMartinus = bot.MarSearch(books.iBooksMar)
    # iMartinus = bot.MarUrl(books.iBooksMarDic, iMartinus)
    # iMarStock = bot.MarStock(books.iBooksMar, iMartinus)
    # if (iMarStock == []) :
    #     print('Vsechny knihy skladem')
    # else :
    #     bot.PrintBooks(iMarStock)

    # print('--------- Megaknihy ---------')
    # iMKSearch = bot.MKSearch(books.iBooks, books.iBooksMK)
    # iMKStock = bot.MKStock(books.iBooks, iMKSearch)
    # bot.PrintBooks(iMKStock)

    # print('--------- ABZKnihy ---------')
    # iABZSearch = bot.ABZSearch(books.iBooks, books.iBooksABZ)
    # bot.PrintBooks(bot.ABZStock(books.iBooks, iABZSearch))

    # print('--------- Knihcentrum ---------')
    # iKCSearch = bot.KCSearch(books.iBooks, books.iBooksKC)
    # bot.PrintBooks(bot.KCStock(books.iBooks, iKCSearch))
    
    # print('--------- Knihy ---------')
    # # needs to add url for all books
    # iKnihySearch = bot.BookSearch(books.UrlKnihy, books.PathKnihy)
    # iKnihyStock = bot.BookStock(iKnihySearch, books.StockKnihy)
    # bot.PrintBooks(iKnihyStock)

    # print('--------- Booktook ---------')
    # iBTSearch = bot.BookSearch(books.UrlBT, books.PathBT)
    # bot.PrintBooks(iBTSearch)
    # bot.PrintBooks(bot.ABZStock(books.iBooks, iABZSearch))
    # in booktook needs to solve problem with xpath for books in stock and not in stock

    # print('--------- sevt ---------')
    # iSevtSearch = bot.BookSearch(books.UrlSevt, books.PathSevt)
    # bot.PrintBooks(bot.BookStock(iSevtSearch, books.StockSevt))


    return 0

if __name__ == '__main__':
    # Source code
    main()
