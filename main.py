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
    bot = bscontrol()
    bot.WebPage(bookstores.iBookstores['Kosmas'])
    iKosmas = bot.KosSearch(books.iBooksKos, books.iRefsKos)
    print('----------Kosmas----------')
    bot.KosStock(iKosmas)

    bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    iDobrovsky = bot.DobrSearch(books.iBooksDobr)
    print('----------Dobrovsky----------')
    # iStock = bot.KosStock(books.iBooks, iTemp)
    iStock = bot.DobrStock(books.iBooksDobr, iDobrovsky)
    for i in range(len(iStock)):
        if(iStock[i].find('neni skladem')):
            print(iStock[i])
        pass

if __name__ == '__main__':
    # Source code
    main()