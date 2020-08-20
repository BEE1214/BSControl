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

    def BookSearch(self, aBook, aRefs):
        iLBook = -1
        iWCount = 1
        # iFind[len(aBook)]
        iFind = []

        for i in range(len(aBook)):
            self.driver.find_element_by_id('search')\
                .send_keys(aBook[i])
            sleep(2)
            self.driver.find_element_by_id('search-btn')\
                .click()
            sleep(2)
            while (iLBook == -1):
                iTemp = self.driver.find_element_by_xpath('//*[@id="js-response-products"]/div/ul/li[{}]'.format(iWCount))
                # iTemp = self.driver.find_element_by_xpath("//li[contains(@data-productinfo, 'name')]")
                if iWCount < 2:
                    iFind.append(iTemp.get_attribute('data-productinfo'))
                else:
                    iFind[i] = iTemp.get_attribute('data-productinfo')
                iLBook = iFind[i].find(aBook[i])
                print(iLBook)
                iWCount += 1
                pass
            iLBook = -1
            iWCount = 1
            # if ((iFounded = iFind.find('Skladem')) != -1):

            
        # print(iFounded)
        # self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(aRefs))\
        #     .click()
        # sleep(2)
        # iStock = self.BookStock()
        # sleep(2)
        # print(iStock) # Later move to dedicaded function for cunting books
        # return iStock
        return iFind

    def BookStock(self):
        iBook = self.driver.find_element_by_xpath('//*[@id="snippet-bookDetail-availabilityInfo"]/div/div[1]/ul/li[1]/a/span[2]')
        if (iBook.text == 'Skladem'):
            return True
        else:
            return False

    def BookCount(self, aBooks, aRefs):
        iBookstock = []
        for i in range(len(aBooks)):
            iStock = self.BookSearch(aBooks[i], aRefs[i])
            sleep(1)
            if (not iStock):
                iBookstock = [aBooks[i]]
            self.driver.find_element_by_xpath('/html/body/div[2]/header/div/p/a')\
                .click()
            sleep(1)
        print(iBookstock)
        return iBookstock

    def WebPage(self, aWebPage):
        # Reduce size of the window for complete program
        # self.driver.set_window_size(100, 100)
        self.driver.set_window_position(-1920,0)
        self.driver.set_window_size(1000, 1080)
        self.driver.get(aWebPage)
        sleep(2)

