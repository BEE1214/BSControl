##=================================##
##=-Project:           BKControl -=##
##=-Author:         Adam Dvorsky -=##
##=-Date:             2020-08-17 -=##
##=================================##

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class bkcontrol:
    def __init__(self):
        self.options = Options()
        self.options.binary_location = '/usr/bin/brave'
        self.driver_path = '/usr/local/bin/chromedriver'
        self.driver = webdriver.Chrome(options = self.options,executable_path = self.driver_path, args='--headless')
        pass

    def BookSearch(self, aBook):
        self.driver.find_element_by_id('search')\
            .send_keys(aBook)
        sleep(2)
        self.driver.find_element_by_id('search-btn')\
            .click()
        sleep(2)
        iBook = self.driver.find_element_by_xpath("//a[contains(@href, '/studijni-predpoklady-a-zaklady-logiky')]")\
            .click()
        iStock = self.BookStock() # Later move to dedicaded function for cunting books

        # self.driver.find_element_by_xpath("//a[contains(@href, '/studijni-predpoklady-a-zaklady-logiky-1-dil')]")\
        #     .click()
        # self.driver.find_element_by_xpath("//a[contains(@class, 'label')]")
        # iSkladem = self.driver.__getattribute__()
        # print(iSkladem)

    def BookStock(self):
        iBook = self.driver.find_element_by_xpath('//*[@id="snippet-bookDetail-availabilityInfo"]/div/div[1]/ul/li[1]/a/span[2]')
        if iBook.text == 'Skladem':
            return True
        else:
            return False

    def BookCount(self, aBooks):
        for i in aBooks:
            BookSearch(aBooks[i])

    def WebPage(self, aWebPage):
        # Reduce size of the window for complete program
        # self.driver.set_window_size(500, 500)
        self.driver.get(aWebPage)
        sleep(2)

