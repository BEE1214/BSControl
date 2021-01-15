##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2021-01-06 -=##
##=================================##
import data.books
from BKControl import bscontrol


class indibscontrol():
    """
    docstring
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
