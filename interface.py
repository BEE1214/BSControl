##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-11-09 -=##
##=================================##
import data.books
import platform
from BKControl import bscontrol
from sys import stdout
from os import system
from time import sleep
import errors


class terminalinterface():
    """
    Basic terminal-based interface for controling bscontrol library
    """
    bot = bscontrol()

    def BookStores(self):
        """
        docstring
        """
        return (
            [
            self.DobrControl,
            self.KosControl,
            self.LuxControl,
            self.MarControl,
            self.MKControl,
            self.ABZControl,
            self.KCControl,
            self.KnihyControl,
            self.BTControl,
            self.SevtControl,
            self.DKControl,
            # self.LadviControl,
            self.UceControl,
            # self.BelControl,
            self.LibControl,
            self.ArchControl,
            self.BooksControl,
            self.LKControl,
            self.AcaControl
            ]
        )

          
    def MainMenu(self):
        """
        Main menu
        """
        ierr = True
        try:
            pass
        except errors.UnknownOS:
            return (print("Unsupported Operating System!"))
        if platform.system() == 'Linux':
            system('clear')
        elif platform.system() == 'Windows':
            system('cls')

        while ierr:
            print('___________________')
            print('     MAIN MENU')
            print('___________________')
            print('(1) Book control')
            print('(2) Emails')
            print('(3) Websites')
            print('(a) About')
            print('(q) Quit')
            ininok = True

            while ininok:
                itermin = input('} ')

                try:
                    if itermin == '1':
                        self.ClearMenu()
                        self.BookControl()
                        ininok = False
                    elif itermin == '2':
                        self.ClearMenu()
                        self.Emails()
                        ininok = False
                    elif itermin == '3':
                        self.ClearMenu()
                        self.Websites()
                        ininok = False
                    elif itermin == 'a':
                        print("Right answer!")
                        ininok = False
                    elif itermin == 'q':
                        self.ClearMenu()
                        print('Closing')
                        return 0
                    elif len(itermin) == 0:
                        continue
                    else:
                        raise errors.InputNotInInterval
                except errors.InputNotInInterval:
                    print('Entered wrong character.\n Try again!')
                    ierr = True
                self.ClearMenu()


    def ClearMenu(self):
        """
        Clear menu
        """
        for i in range(1,57):
            stdout.write('\x1b[1A')
            stdout.write('\x1b[2K')

            
    def Websites(self):
        """
        Website menu
        """
        iCon = True

        while iCon:
            self.BSHeader('Websites')
            self.BSMenu()
            iWeb = input('} ')
            self.ClearMenu()
            try:
                iLegend = data.books.bookstores.iLegend
                iUrl = data.books.bookstores.iUrl
                if iWeb == 'p':
                    iCon = False
                elif len(iWeb) == 0:
                    for i in range(len(iLegend)):
                        print(f'{iLegend[i]}:\n{iUrl[iLegend[i]]}')
                    input('')
                elif len(iWeb) < 3 and int(iWeb) < len(iLegend):
                    print(f'\n{iLegend[int(iWeb)-1]}:\n {iUrl[iLegend[int(iWeb)-1]]}')
                    input('')
                else:
                    raise errors.InputWrong
            except errors.InputWrong:
                print('Wrong number')
                sleep(4)
            except ValueError:
                print('Wrong character!')
                sleep(4)
            self.ClearMenu()

    def Emails(self):
        """
        Emails menu
        """
        icon = True

        while icon:
            # stdout.flush()
            # scroll one line up
            # delete that line
            self.BSHeader('Emails')
            self.BSMenu()
            iWeb = input('} ')
            self.ClearMenu()

            try:
                iLegend = data.books.bookstores.iLegend
                iUrl = data.books.bookstores.iEmails
                if iWeb == 'p':
                    icon = False
                elif len(iWeb) == 0:
                    for i in range(len(iLegend)):
                        print(f'{iLegend[i]}:\n{iUrl[iLegend[i]]}')
                    input('')
                elif len(iWeb) < 3 and int(iWeb) < 19:
                    print(f'\n{iLegend[int(iWeb)-1]}:\n {iUrl[iLegend[int(iWeb)-1]]}')
                    input('')
                else:
                    raise errors.InputWrong
            except errors.InputWrong:
                print('Wrong number')
                sleep(4)
            except ValueError:
                print('Wrong character!')
                sleep(4)
            self.ClearMenu()

    def BSMenu(self):
        """
        Prints menu for bookstore choice
        """
        print('(1)  Dobrovsky')      # 1  -
        print('(2)  Kosmas')         # 2  -
        print('(3)  Luxor')          # 3  -
        print('(4)  Martinus')       # 4  -
        print('(5)  Megaknihy')      # 5  -
        print('(6)  ABZ Knihy')      # 6  -
        print('(7)  Knihcentrum')    # 7  -
        print('(8)  Knihy.cz')       # 8  -
        print('(9)  Booktook')       # 9  -
        print('(10) Sevt')           # 10 -
        print('(11) Dumknihy')       # 11 -
        print('(12) Ladvi')          # 12 -
        print('(13) Ucebnice')       # 13 -
        print('(14) Beletrie')       # 14 -
        print('(15) Libristo')       # 15 -
        print('(16) Knizniarcha')    # 16 -
        print('(17) Books.cz')       # 17 -
        print('(18) Levne-knihy')    # 18 -
        print('(19) Academia')       # 19 -
        print('(p)  previous menu')
        print('Choose websites to display(all=default, 1, 2, 3, etc)')

    def BSHeader(self, aHead):
        """
        Prints header of menu
        """
        print('___________________')
        print(f'     {aHead}')
        print('___________________')

    def BookList(self):
        """
        List all books in database that are being checked.

        Returns:
            iBooks(list): list of books
        """
        iBooks = data.books.books.iBooks
        for i in range(len(iBooks)):
            if i > 9:
                print(f'{i+1}. {iBooks[i]}')
            else:
                print(f'{i+1}.  {iBooks[i]}')
        input('')
        self.ClearMenu()
        return iBooks

    def BookControl(self):
        """
        Menu for book control
        """
        while True:
            iEnt = True
            self.BSHeader('BOOK CONTROL')
            print('(1) Check bookstore')
            print('(2) List all available bookstores')
            print('(3) List all books')
            print('(0) Main menu')
            iIn = input('} ')

            while iEnt:
                if iIn == '1':
                    self.ControlBookStore()
                    self.ClearMenu()
                    iEnt = False
                elif iIn == '2':
                    self.ClearMenu()
                    self.AvBookStores()
                    iEnt = False
                elif iIn == '3':
                    self.ClearMenu()
                    self.BookList()
                    iEnt = False
                elif iIn == '0':
                    iEnt = False
                    return 0
                else:
                    iIn = input('} ')
                    iEnt = True

    def AvBookStores(self):
        """
        Print all checked bookstores. Only their names.
        """
        self.ClearMenu()
        iLegend = data.books.bookstores.iLegend
        for i in range(len(iLegend)):
            if i > 9:
                print(f'{i+1}. {iLegend[i]}')
            else:
                print(f'{i+1}.  {iLegend[i]}')
        input('')
        self.ClearMenu()


    def AllControlBookStores(self):
        """
        Control availability of books on bookstores
        """
        iBookStores = self.BookStores()
        for i in range(len(iBookStores)):
            print(f'Checking {data.books.bookstores.iLegend[i]}')
            iBookStores[i]()

        return 0

    def ControlBookStore(self):
        """
        docstring
        """
        iBookStores = self.BookStores()
        self.ClearMenu()

        print('(Enter) Check all bookstores')
        for i in range(len(data.books.bookstores.iLegend)):
            print(f'({i + 1}) {data.books.bookstores.iLegend[i]}')
        BookStore = input('} ')

        try:
            if BookStore == '':
                self.ClearMenu()
                self.AllControlBookStores()
            elif BookStore.isnumeric() and len(BookStore) == 1:
                self.ClearMenu()
                iBookStores[int(BookStore) - 1]()
            else:
                raise errors.InputWrong
        except errors.InputWrong:
            print('Input is not number or has more then 1 digit')
                


    def DobrControl(self):
        """
        Dobrovsky book control
        """
        
        self.bot.BSStock(data.books.books.UrlDobr, data.books.books.PathDobr, data.books.books.StockDobr)
    
    def KosControl(self):
        """
        Kosmas book control
        """
        
        self.bot.BSStock(data.books.books.UrlKos, data.books.books.PathKos, data.books.books.StockKos)
    
    def LuxControl(self):
        """
        Luxor book control
        """
        
        self.bot.BSStock(data.books.books.UrlLux, data.books.books.PathLux, data.books.books.StockLux)
    
    def MarControl(self):
        """
        Martinus book control
        """
        
        self.bot.BSStock(data.books.books.UrlMar, data.books.books.PathMar, data.books.books.StockMar)
    
    def MKControl(self):
        """
        Megaknihy book control
        """
        
        self.bot.BSStock(data.books.books.UrlMK, data.books.books.PathMK, data.books.books.StockMK)
    
    def ABZControl(self):
        """
        ABZ Knihy book control
        """
        
        self.bot.BSStock(data.books.books.UrlABZ, data.books.books.PathABZ, data.books.books.StockABZ)
    
    def KCControl(self):
        """
        Knihcentrum book control
        """
        
        self.bot.BSStock(data.books.books.UrlKC, data.books.books.PathKC, data.books.books.StockKC)
    
    def KnihyControl(self):
        """
        Knihy.cz book control
        """
        
        self.bot.BSStock(data.books.books.UrlKnihy, data.books.books.PathKnihy, data.books.books.StockKnihy)
    
    def BTControl(self):
        """
        Booktook book control
        """
        
        self.bot.BSStock(data.books.books.UrlBT, data.books.books.PathBT, data.books.books.StockBT)
    
    def SevtControl(self):
        """
        SEVT book control
        """
        
        self.bot.BSStock(data.books.books.UrlSevt, data.books.books.PathSevt, data.books.books.StockSevt)
    
    def DKControl(self):
        """
        Dumknihy book control
        """
        
        self.bot.BSStock(data.books.books.UrlDK, data.books.books.PathDK, data.books.books.StockDK)
    
    def LadviControl(self):
        """
        Ladvi book control
        """
        
        self.bot.BSStock(data.books.books.UrlLadvi, data.books.books.PathLadvi, data.books.books.StockLadvi)
    
    def UceControl(self):
        """
        Ucebnice book control
        """
        
        self.bot.BSStock(data.books.books.UrlUce, data.books.books.PathUce, data.books.books.StockUce)
    
    def BelControl(self):
        """
        Beletrie book control
        """
        
        self.bot.BSStock(data.books.books.UrlBel, data.books.books.PathBel, data.books.books.StockBel)
    
    def LibControl(self):
        """
        Libristo book control
        """
        
        self.bot.BSStock(data.books.books.UrlLib, data.books.books.PathLib, data.books.books.StockLib)
    
    def ArchControl(self):
        """
        Knizniarcha.cz book control
        """
        
        self.bot.BSStock(data.books.books.UrlArch, data.books.books.PathArch, data.books.books.StockArch)
    
    def BooksControl(self):
        """
        Books.cz book control
        """
        
        self.bot.BSStock(data.books.books.UrlBooks, data.books.books.PathBooks, data.books.books.StockBooks)
    
    def LKControl(self):
        """
        Levne-knihy book control
        """
        
        self.bot.BSStock(data.books.books.UrlLK, data.books.books.PathLK, data.books.books.StockLK)
    
    def AcaControl(self):
        """
        Academia book control
        """
        
        self.bot.BSStock(data.books.books.UrlAca, data.books.books.PathAca, data.books.books.StockAca)
    

 