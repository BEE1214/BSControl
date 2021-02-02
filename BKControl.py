##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep
from tologfile import tologfile
import errors

class bscontrol:
    """ Library with functions for checking books in stock on certain bookstores.

    Dependencies:
        - python 3.8.5
        - selenium
        On linux:
            - Brave browser
        On windows:
            - Google Chrome or Chromium
        - webdriver for actual version of Brave/Chrome browser
    """
    def __init__(self):
        if (system() == 'Linux'):
            self.options = Options()
            self.options.binary_location = '/usr/bin/brave'
            self.driver_path = '/usr/local/bin/chromedriver'
            self.driver = webdriver.Chrome(options = self.options,executable_path = self.driver_path)
            # self.driver.set_window_size(1300, 1080)
        elif (system() == 'Windows'):
            # self.options = Options()
            # self.options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
            self.driver_path = r'C:/Users/adamd/Apps/Chromdriver/chromedriver.exe'
            self.driver = webdriver.Chrome(executable_path=self.driver_path)
            # self.driver.set_window_position(-1920,0)
            self.driver.set_window_size(1080, 1080)
        else:
            raise errors.UnknownOS
    
    def __del__(self):
        self.driver.close()

# ===================== BookSearch ======================== #
    def BookSearch(self, aUrl, aPath):
        """
        Args:
            aUrl(list): url of bookstore
            aPath(dictionary): xpath for element on page
        Returns:
            iSearch(list): list of searched books with their stock status
        """
        iSearch = [aPath['BookStore']]

        for i in range(len(aUrl)):
            self.WebPage(aUrl[i])
            try:
                name = self.driver.find_element_by_xpath(aPath["name"]).text
            except NoSuchElementException:
                print('Couldn\'t find name element on webpage')
            except TimeoutException:
                print('Your internet is too much of a potato')
            try:
                stock = self.driver.find_element_by_xpath(aPath["url"]).text
                sleep(1)
                iSearch.append(f'{name} - {stock}')
            except NoSuchElementException:
                iSearch.append(f'{name} - neni na skladu')
            except TimeoutException:
                print('Your internet is too much of a potato')
        return iSearch

# ===================== BookStock ========================= #
    def BookStock(self, aBooks, aStock):
        """
        Args:
            aBooks(list): list of books with their stock status
            aStock(string): key word for stock option for different pages
        Returns:
            iStock(list): list of books not in stock
        """
        # iStock = [aStock[0]]
        iStock = []

        for i in range(len(aBooks)):
            if(aBooks[i].find(aStock) == -1):
                iStock.append(f'{aBooks[i]}')

        if (iStock == []):
            iStock.append('Vse skladem')
            
        return iStock


# ===================== PrintBook ======================== #
    def PrintBooks(self, aStock):
        """ Simple list printing function.
        """
        for i in range(len(aStock)):
            print(aStock[i])
        pass
    
# =================== BookFucntions ======================= #
    def BSStock(self, aUrl, aPath, aStock):
        """ Goes throught list of urls, finds state of books on those pages and prints books that aren't in stock.

        Args:
            aUrl (list): list of urls
            aPath (dictionary): contains name and stock with xpath
            aStock (string): term for book in stock

        Returns:
            list: list of books that are not in stock
        """
        iSearch = self.BookSearch(aUrl, aPath)
        iStock = self.BookStock(iSearch, aStock)
        tologfile('Search.log').tofile(iSearch)
        tologfile('Stock.log').tofile(iStock)
        self.PrintBooks(iStock)
        return iStock

# ==================== PageLookup ========================= #
    def WebPage(self, aWebPage):
        # Reduce size of the window for complete program
        # self.driver.set_window_size(100, 100)
        self.driver.get(aWebPage)
        sleep(2)

