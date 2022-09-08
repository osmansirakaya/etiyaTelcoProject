from cgitb import text
import email
from itertools import tee
from multiprocessing.sharedctypes import Value
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Test_uc08_tc04:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-contact-form/1")
        self.driver.maximize_window()
        sleep(2)
    #Email alanının boş bırakılması durumu
    def test_contactmediumupdateemptyemail(self):
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")               
        email.clear()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        bytton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
        bytton.click()
        

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")))
        savebutton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")               
        savebutton.click()
        sleep(1)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-custom-toast/p-toast/div/p-toastitem/div/div/div/p")))
        error=self.driver.find_element(By.XPATH,"/html/body/app-root/app-custom-toast/p-toast/div/p-toastitem/div/div/div/p")               
        errortext = "Please fill required areas!"
        errormedium=error.get_attribute("value")
        #errormedium= email.text
        assert errormedium == errortext
        assert error.is_displayed

        


    #MobilePhone alanının boş bırakılması durumu
    def test_contactmediumupdateemptymphone(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               
        mphone.clear()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")))
        savebutton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")               
        savebutton.click()
        sleep(1)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-custom-toast/p-toast/div/p-toastitem/div/div/div/p")))
        error=self.driver.find_element(By.XPATH,"/html/body/app-root/app-custom-toast/p-toast/div/p-toastitem/div/div/div/p")               
        errortext = "Please fill required areas!"
        errormedium=error.get_attribute("value")
        #errormedium= email.text
        assert errormedium == errortext
        assert error.is_displayed
    
    def teardown_method(self):
        self.driver.quit()