##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bscontrol
from tologfile import tologfile
from data.books import books
from data.books import bookstores
from datetime import time

def main():
    bot = bscontrol()
    # iLoop = False
    
    # while True:
    # print('---------- Kosmas ----------')
    # bot.BSStock(books.UrlKos, books.PathKos, books.StockKos)

    # print('---------- Dobrovsky ----------')
    # bot.BSStock(books.UrlDobr, books.PathDobr, books.StockDobr)
    
    # print('---------- Luxor ----------')
    # bot.BSStock(books.UrlLux, books.PathLux, books.StockLux)

    # print('---------- Martinus ----------')
    # bot.BSStock(books.UrlMar, books.PathMar, books.StockMar)

    # print('--------- Megaknihy ---------')
    # bot.BSStock(books.UrlMK, books.PathMK, books.StockMK)

    # print('--------- ABZKnihy ---------')
    # bot.BSStock(books.UrlABZ, books.PathABZ, books.StockABZ)

    # print('--------- Knihcentrum ---------')
    # bot.BSStock(books.UrlKC, books.PathKC, books.StockKC)
    
    # print('--------- Knihy ---------')
    # # # needs to add url for all books
    # bot.BSStock(books.UrlKnihy, books.PathKnihy, books.StockKnihy)

    # print('--------- Booktook ---------')
    # # in booktook needs to solve problem with xpath for books in stock and not in stock
    # bot.BSStock(books.UrlBT, books.PathBT, books.StockBT)

    # print('--------- sevt ---------')
    # bot.BSStock(books.UrlSevt, books.PathSevt, books.StockSevt)

    # print('--------- DumKnihy ---------')
    # # "Jak se dostat na vysokou skolu" is missing in list
    # bot.BSStock(books.UrlDK, books.PathDK, books.StockDK)

    # print('--------- Ladvi ---------')
    # bot.BSStock(books.UrlLadvi, books.PathLadvi, books.StockLadvi)

    # print('-------- Ucebnice ---------')
    # bot.BSStock(books.UrlUce, books.PathUce, books.StockUce)
    
    # print('-------- Beletrie ---------')
    # bot.BSStock(books.UrlBel, books.PathBel, books.StockBel)

    # print('--------- Knizniarcha ----------')
    # bot.BSStock(books.UrlArch, books.PathArch, books.StockArch)
    # print('studijni predpoklady, lekarskou 1 a 2, anglictina, nemcina pravnicka 1 a 2 nemaji vubec v nabidce')

    # books.cz
    bot.BSStock(books.UrlBooks, books.PathBooks, books.StockBooks)

    # levne-knizky
    bot.BSStock(books.UrlLK, books.PathLK, books.StockLK)

    return 0

if __name__ == '__main__':
    # Source code
    main()
