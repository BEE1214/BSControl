##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from platform import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class bscontrol:
    def __init__(self):
        if (system() == 'Linux'):
            self.options = Options()
            self.options.binary_location = '/usr/bin/brave'
            self.driver_path = '/usr/local/bin/chromedriver'
            self.driver = webdriver.Chrome(options = self.options,executable_path = self.driver_path)
        elif (system() == 'Windows'):
            # self.options = Options()
            # self.options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
            self.driver_path = r'C:/Users/adamd/Apps/Chromdriver/chromedriver.exe'
            self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def DobrSearch(self, aBooks):
        """ 
        Search on dobrovskyknihy.cz
        Searches for information about aBooks on current web page.

        args:
            - aBooks - list of books
        Returns:
            - iFind - list of founded informations
        """
        iLBook = -1
        iWCount = 1
        # iFind[len(aBook)]
        iFind = []

        for i in range(len(aBooks)):
            self.driver.find_element_by_id('search')\
                .send_keys(aBooks[i])
            sleep(3)
            self.driver.find_element_by_id('search-btn')\
                .click()
            sleep(3)
            while (iLBook == -1):
                iTemp = self.driver.find_element_by_xpath('//*[@id="js-response-products"]/div/ul/li[{}]'.format(iWCount))
                # iTemp = self.driver.find_element_by_xpath("//li[contains(@data-productinfo, 'name')]")
                if iWCount < 2:
                    iFind.append(iTemp.get_attribute('data-productinfo'))
                elif(iWCount == 5):
                    pass
                else:
                    iFind[i] = iTemp.get_attribute('data-productinfo')
                iLBook = iFind[i].find(aBooks[i])
                # print(iLBook)
                iWCount += 1
                pass
            iLBook = -1
            iWCount = 1
            # if ((iFounded = iFind.find('Skladem')) != -1):
        pass
            
        return iFind

    def DobrStock(self, aBook, aBookinfo):
        """ 
        arg:
            - aFind - list of books with their availability
            - aBooks - list of books
        return:
            - iStock - list of books that are in stock
        """

        iStock = []
        iBook = aBook
        iBookinfo = aBookinfo

        for i in range(len(iBookinfo)):
            if ((iBookinfo[i].find('Skladem') != -1) and (iBookinfo[i].find('Skladem (vybrané prodejny)') == -1) and (iBookinfo[i].find('Skladem u') == -1)):
                iStock.append(f'{iBook[i]} - skladem')
            elif(iBookinfo[i].find('Skladem (vybrané prodejny)') != -1):
                iStock.append(f'{iBook[i]} - neni skladem')
            else:
                iStock.append(f'{iBook[i]} - neni skladem')

        return iStock

    def LuxSearch(self, aBooks, aRefs):
        """ 
        Search on luxor.cz
        Searches for information about aBooks on current web page.

        args:
            - aBooks - list of books
            - aRefs - list modified for href
        Returns:
            - iFind - list of founded informations
        """

        iFind = []

        for i in range(len(aBooks)):
            self.WebPage(aRefs[aBooks[i]])
            iText = self.driver.find_element_by_xpath('//div[contains(@class, "f1ubm3q7")]').text
            iFind.append(f'{iText}')
        pass
        
        return iFind

    def LuxStock(self, aFind, aBooks):
        """ 
        arg:
            - aFind - list of books with their availability
            - aBooks - list of books
        return:
            - iStock - list of books that are in stock
        """
        iStock = ['Luxor']
        for i in range(len(aBooks)):
            if (aFind[i].find('NENÍ SKLADEM') != -1):
                iStock.append(f'{aBooks[i]} - neni skladem')
                pass
        
        return iStock

    def KosSearch(self, aBooks, aRefs):
        """ 
        Search on kosmas.cz
        Searches for information about aBooks on current web page.

        args:
            - aBooks - list of books
            - aRefs - list modified for href
        Returns:
            - iFind - list of founded informations
        """

        # iLBook = -1
        # iWCount = 1
        iFind = []

        for i in range(len(aBooks)):
            self.driver.find_element_by_id('searchInput')\
                .send_keys(aBooks[i])
            # sleep(3)
            self.driver.find_element_by_id('searchButton')\
                .click()
            # sleep(2)
            self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(aRefs[i]))\
                .click()
            iTemp = self.driver.find_element_by_xpath("//td[contains(@class, 'availability')]")
            iText = iTemp.text
            # print(iText)
            iFind.append(f'{aBooks[i]} - {iText}')
                # print(f'{aBooks[i]} - skladem')
        pass
        
        return iFind

    def KosStock(self, aStock):
        """ 
        arg:
            - aFind - list of books with their availability
            - aBooks - list of books
        return:
            - iStock - list of books that are in stock
        """

        for i in range(len(aStock)):
            if aStock[i].find('Skladem') == -1 :
                print(aStock[i])
            pass
        pass

    def BookStock(self):
        """ 
        arg:
            - aFind - list of books with their availability
            - aBooks - list of books
        return:
            - iStock - list of books that are in stock
        """

        iBook = self.driver.find_element_by_xpath('//*[@id="snippet-bookDetail-availabilityInfo"]/div/div[1]/ul/li[1]/a/span[2]')
        if (iBook.text == 'Skladem'):
            return True
        else:
            return False

    def WebPage(self, aWebPage):
        # Reduce size of the window for complete program
        # self.driver.set_window_size(100, 100)
        self.driver.set_window_position(-1920,0)
        self.driver.set_window_size(1300, 1080)
        self.driver.get(aWebPage)
        sleep(2)

