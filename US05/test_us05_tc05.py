from cgitb import text
import email
import pytest
import contants_us05
from operator import contains
from itertools import tee
from multiprocessing.sharedctypes import Value
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Test_us05_tc05:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-dashboard")
        self.driver.maximize_window()
        sleep(2)

        #Yeni Müsteri Oluşturma -> başka bi kullanıcı ile eşleşen nationality id kontrolü
    def createCustomer(self):       
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")))
        createCustomerClick = self.driver.find_element
        (By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")
        sleep(2)
        createCustomerClick .click()



    def teardown_method(self):
        self.driver.quit()

    