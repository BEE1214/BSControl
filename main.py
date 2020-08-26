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
    # bot.WebPage(bookstores.iBookstores['Kosmas'])
    # iKosmas = bot.KosSearch(books.iBooksKos, books.iRefsKos)
    # print('----------Kosmas----------')
    # bot.KosStock(iKosmas)

    # bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    # iDobrovsky = bot.DobrSearch(books.iBooksDobr)
    # print('----------Dobrovsky----------')
    # # iStock = bot.KosStock(books.iBooks, iTemp)
    # iStock = bot.DobrStock(books.iBooksDobr, iDobrovsky)
    # for i in range(len(iStock)):
    #     if(iStock[i].find('neni skladem') != -1):
    #         print(iStock[i])
    #     pass
    
    # bot.WebPage(bookstores.iBookstores['Luxor'])
    iLuxor = bot.LuxSearch(books.iBooksLux, books.iRefsLux)
    iLuxStock = bot.LuxStock(iLuxor, books.iBooksLux)
    for i in range(len(iLuxStock)):
        print(iLuxStock[i])
    pass

if __name__ == '__main__':
    # Source code
    main()

    # //*[@id="product-list-content"]/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/a[1]