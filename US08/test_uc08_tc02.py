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


class Test_uc08_tc02:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-contact-form/1")
        self.driver.maximize_window()
        sleep(2)

    #"Contact Medium Update" sayfasındaki seçenekler görünür, tıklanabilir ve görünebilir olmalı.
    def test_contactmediumupdatepage(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")               
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        homephone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
       
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")               

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")))
        savebuttondisplayed=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")               
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[1]/button")))
        cancelbuttondisplayed=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[1]/button")               
        
        assert email.is_displayed
        assert mphone.is_displayed
        assert homephone.is_displayed
        assert fax.is_displayed
        assert savebuttondisplayed.is_selected
        assert cancelbuttondisplayed.is_selected

    #Ekranda bulunan E-mail*, Mobile Phone*, Home Phone ve Fax Alanları görünür ve değer girilebilir olmalı.
    def test_contactmediumupdatepagechange(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")               
        email.clear()
        email.send_keys("kaganulupinar@gmail.com")
        emailvalue = email.get_attribute("value")
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        homephone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
        homephone.clear()
        homephone.send_keys("3122827882")
        homevalue = homephone.get_attribute("value")
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")               
        fax.clear()
        fax.send_keys("3122823456")
        faxvalue = fax.get_attribute("value")
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               
        mphone.clear()
        mphone.send_keys("3124567890")
        mphonevalue = mphone.get_attribute("value")
        sleep(1)

        assert emailvalue == ("kaganulupinar@gmail.com")
        assert homevalue == ("3122827882")
        assert faxvalue == ("3122823456")
        assert mphonevalue == ("3124567890")
    
    def teardown_method(self):
        self.driver.quit()

    