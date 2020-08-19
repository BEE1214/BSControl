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

class controldobrovsky:
    def __init__(self):
        if system() == 'Linux':
            self.options = Options()
            self.options.binary_location = '/usr/bin/brave'
            self.driver_path = '/usr/local/bin/chromedriver'
            self.driver = webdriver.Chrome(options = self.options,executable_path = self.driver_path)
        elif system() == 'Windows':
            self.driver = webdriver.Chrome(executable_path=r'C:/Users/adamd/Apps/Chromdriver/chromedriver.exe')

    def BookSearch(self, aBook, aRefs):
        self.driver.find_element_by_id('search')\
            .send_keys(aBook)
        sleep(2)
        self.driver.find_element_by_id('search-btn')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(aRefs))\
            .click()
        sleep(2)
        iStock = self.BookStock()
        sleep(2)
        print(iStock) # Later move to dedicaded function for cunting books
        return iStock

    def BookStock(self):
        iBook = self.driver.find_element_by_xpath('//*[@id="snippet-bookDetail-availabilityInfo"]/div/div[1]/ul/li[1]/a/span[2]')
        if iBook.text == 'Skladem':
            return True
        else:
            return False

    def BookCount(self, aBooks, aRefs):
        iBookstock = []
        for i in range(len(aBooks)):
            iStock = self.BookSearch(aBooks[i], aRefs[i])
            sleep(1)
            if not iStock:
                iBookstock = [aBooks[i]]
            self.driver.find_element_by_xpath('/html/body/div[2]/header/div/p/a')\
                .click()
            sleep(1)
        print(iBookstock)
        return iBookstock

    def WebPage(self, aWebPage):
        # Reduce size of the window for complete program
        # self.driver.set_window_size(100, 100)
        self.driver.set_window_size(1080, 800)
        self.driver.get(aWebPage)
        sleep(2)

