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

    # print('---------- Dobrovsky ----------')
    # iDobrovskySearch = bot.BookSearch(books.UrlDobr, books.PathDobr)
    # iDobrStock = bot.BookStock(iDobrovskySearch, books.StockDobr)
    # bot.PrintBooks(iDobrStock)

    
    # print('---------- Luxor ----------')
    # iLuxSearch = bot.BookSearch(books.UrlLux, books.PathLux)
    # iLuxStock = bot.BookStock(iLuxSearch, books.StockLux)
    # bot.PrintBooks(iLuxStock)


    # print('---------- Martinus ----------')
    # iMarSearch = bot.BookSearch(books.UrlMar, books.PathMar)
    # iMarStock = bot.BookStock(iMarSearch, books.StockMar)
    # bot.PrintBooks(iMarStock)

    # print('--------- Megaknihy ---------')
    # iMKSearch = bot.BookSearch(books.UrlMK, books.PathMK)
    # iMKStock = bot.BookStock(iMKSearch, books.StockMK)
    # bot.PrintBooks(iMKStock)

    # print('--------- ABZKnihy ---------')
    # iABZSearch = bot.BookSearch(books.UrlABZ, books.PathABZ)
    # iABZStock = bot.BookStock(iABZSearch, books.StockABZ)
    # bot.PrintBooks(iABZStock)

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

    print('--------- DumKnihy ---------')
    iDKSearch = bot.BookSearch(books.UrlDK, books.PathDK)
    iDKStock = bot.BookStock(iDKSearch, books.StockDK)
    bot.PrintBooks(iDKStock)
    # "Jak se dostat na vysokou skolu" is missing in list

    return 0

if __name__ == '__main__':
    # Source code
    main()
