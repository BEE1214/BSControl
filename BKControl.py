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

