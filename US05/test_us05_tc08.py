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

class Test_tcmb:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/add-address-info")
        self.driver.maximize_window()
        sleep(2)

    def test_contactMediumExit(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[1]/div/div[2]/div/select")))
        city = self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[1]/div/div[2]/div/select")
        sleep(2)
        city.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[1]/div/div[2]/div/select/option[8]")))
        optionSelect = self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[1]/div/div[2]/div/select/option[8]")
        sleep(2)
        optionSelect.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input")))
        houseNumber = self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input")        
        houseNumber.send_keys("8")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[3]/div/div[2]/input")))
        street= self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[3]/div/div[2]/input")        
        street.send_keys("Gamze Özdemir Cad.")


        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[4]/div/div[2]/textarea")))
        addDes = self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[4]/div/div[2]/textarea")        
        addDes.send_keys("ankara")

        #address info sayfasında aşağı kaydırma
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        sleep(3)

        #address info sayfasında save alanına tıklar
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[2]/div/button")))
        saveClick = self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[2]/div/button")
        sleep(3)
        saveClick.click()
        sleep(3)

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP)
        actions.perform()

         #address info sayfasında aşağı kaydırma
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        #address info sayfasında next alanına tıklar
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[4]/button[2]")))
        nextClick= self.driver.find_element(By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[4]/button[2]")
        sleep(3)
        nextClick.click()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[3]/div/div/button")))
        previousClick = self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[3]/div/div/button")
        sleep(2)
        previousClick .click()
        sleep(2)

        sleep(3)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/th")))
        cityInfo=self.driver.find_element(By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/th")
        assert cityInfo.text == "Dallas"

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/td[1]")))
        streetName=self.driver.find_element(By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/td[1]")
        assert streetName.text == "Gamze Özdemir Cad."

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/td[2]")))
        HouseNumber=self.driver.find_element(By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/td[2]")
        assert HouseNumber.text == "8"

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/td[3]")))
        addressDes=self.driver.find_element(By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[2]/div/app-table-info/div/table/tbody/tr/td[3]")
        assert addressDes.text == "ankara"


    def teardown_method(self):
        self.driver.quit()