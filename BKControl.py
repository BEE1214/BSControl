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

class bscontrol:
    def __init__(self):
        if (system() == 'Linux'):
            self.options = Options()
            self.options.binary_location = '/usr/bin/brave'
            self.driver_path = '/usr/local/bin/chromedriver'
            self.driver = webdriver.Chrome(options = self.options,executable_path = self.driver_path)
            self.driver.set_window_position(-1920,0)
            self.driver.set_window_size(1300, 1080)
        elif (system() == 'Windows'):
            # self.options = Options()
            # self.options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
            self.driver_path = r'C:/Users/adamd/Apps/Chromdriver/chromedriver.exe'
            self.driver = webdriver.Chrome(executable_path=self.driver_path)
            self.driver.set_window_position(-1920,0)
            self.driver.set_window_size(1300, 1080)


# ================== Dobrovsky =======================
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

# ==================== Luxor =========================
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

# =================== Kosmas =========================
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
            - aStock - list of books with their availability
        return:
            - inStock - list of books that aren't in stock
        """
        inStock = []
        for i in range(len(aStock)):
            if aStock[i].find('Skladem') == -1 :
                inStock.append(aStock[i])
            pass
        return inStock
    
# ================== Martinus ========================
    def MarSearch(self, aBooks):
        """
        Search on martinus.cz
        Searches for information about aBooks on current web page.

        args:
            - aBooks - list of books
        Returns:
            - iFind - list of founded informations
        """

        iFind = []
        iLBook = -1
        iCount = 2

        for i in range(len(aBooks)):
            self.driver.find_element_by_id('search-in-header')\
                .send_keys(aBooks[i])
            self.driver.find_element_by_id('search-in-header')\
                .send_keys(Keys.RETURN)
            sleep(2)
            while (iLBook == -1):
                # //*[@id="page-container"]/main/section[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/h2/a
                iPrint = self.driver.find_element_by_xpath(
                    f'//*[@id="page-container"]/main/section[2]/div/div/div[2]/div[{iCount}]'
                    )
                iLBook = iPrint.text.find(aBooks[i])
                if (iLBook != -1):
                    self.driver.find_element_by_xpath(
                        f'//*[@id="page-container"]/main/section[2]/div/div/div[2]/div[{iCount}]/div/div[1]/div/div[2]/div[1]/h2/a'
                    ).click()
                    pass
                iCount += 1
                pass
            sleep(2)
            iFind.append(self.driver.find_element_by_xpath('//p[contains(@class, "mj-delivery-time mb-small text-color-grey-dark")]').text)
            iCount = 2
            iLBook = -1
        return iFind

    def MarUrl(self, aUrl, aFind):
        iFind = aFind

        for i in range(len(aUrl)):
            try:
                self.WebPage(aUrl[i])
                iFind.append(self.driver.find_element_by_xpath('//p[contains(@class, "mj-delivery-time mb-small text-color-grey-dark")]').text)
            except:
                print('Cannot locate element')

        return iFind
        
    def MarStock(self, aBooks, aFind):
        iStock = []
        for i in range(len(aBooks)):
            if (aFind[i].find('Na skladě') == -1):
                iStock.append(f'{aBooks[i]} - neni skladem')
                pass
            pass
        return iStock

# ================== Megaknihy =======================
    def MKSearch(self, aBooks, aRefs) :
        iSearch = []

        for i in range(len(aBooks)):
            self.WebPage(aRefs[aBooks[i]])
            iSearch.append(self.driver.find_element_by_xpath(
                            '//span[contains(@class, "avail_now_text")]'
                            ).text)

        return iSearch

    def MKStock(self, aBooks, aSearch):
        iStock = []

        for i in range(len(aBooks)):
            if(aSearch[i].find('máme skladem') == -1):
                iStock.append(f'{aBooks[i]} - neni skladem')

        return iStock

# ================== ABZKnihy ========================
    def ABZSearch(self, aBooks, aRefs):
        iSearch = []

        for i in range(len(aBooks)):
            self.WebPage(aRefs[aBooks[i]])
            iSearch.append(self.driver.find_element_by_xpath('//div[contains(@class, "prices_1_real")]').text)
        return iSearch

    def ABZStock(self, aBooks, aSearch):
        iStock = []

        for i in range(len(aBooks)):
            if(aSearch[i].find('je skladem') == -1):
                iStock.append(f'{aBooks[i]} - neni skladem')

        return iStock

# ================== Knihcentrum =====================
    def KCSearch(self, aBooks, aRefs):
        iSearch = []

        for i in range(len(aBooks)):
            self.WebPage(aRefs[aBooks[i]])
            iSearch.append(self.driver.find_element_by_xpath('//span[contains(@class, "stock-name")]').text)
        return iSearch

    def KCStock(self, aBooks, aSearch):
        iStock = []

        for i in range(len(aBooks)):
            if(aSearch[i].find('IHNED odesíláme') == -1) and (aSearch[i].find('poslední kusy') == -1):
                iStock.append(f'{aBooks[i]} - neni skladem')

        return iStock

# ===================== BookSearch ========================
    def BookSearch(self, aUrl, aPath):
        """
        arg:
            aUrl - url of bookstore
            aPath - xpath for element on page
        return:
            iSearch - list of searched books with their stock status
        """
        iSearch = []

        for i in range(len(aUrl)):
            self.WebPage(aUrl[i])
            try:
                name = self.driver.find_element_by_xpath(aPath["name"]).text
            except NoSuchElementException:
                print('No such element on webpage')
            except TimeoutException:
                print('Your internet is too much of a potato')
            try:
                stock = self.driver.find_element_by_xpath(aPath["url"]).text
                iSearch.append(f'{name} - {stock}')
            except NoSuchElementException:
                iSearch.append(f'{name} - neni skladem')
            except TimeoutException:
                print('Your internet is too much of a potato')
        return iSearch

    def BookStock(self, aBooks, aStock):
        """
        arg:
            aBooks - list of books with their stock status
            aStock - key word for stock option for different pages
        return:
            iStock - list of books not in stock
        """
        iStock = []

        for i in range(len(aBooks)):
            if(aBooks[i].find(aStock) == -1):
                iStock.append(f'{aBooks[i]}')

        if (iStock == []):
            iStock.append('Vse skladem')
            
        return iStock


    def PrintBooks(self, aStock):
        """
        Simple list printing function.
        """
        for i in range(len(aStock)):
            print(aStock[i])
        pass

    def WebPage(self, aWebPage):
        # Reduce size of the window for complete program
        # self.driver.set_window_size(100, 100)
        self.driver.get(aWebPage)
        sleep(2)

