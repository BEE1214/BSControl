##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from BKControl import bkcontrol
from data.books import books
from data.bookstores import bookstores

def main():
    bot = bkcontrol()
    bot.WebPage(bookstores.iBookstores['Dobrovsky'])
    bot.BookSearch(books.iBooks[0])

    pass

if __name__ == '__main__':
    # Source code
    main()
    pass