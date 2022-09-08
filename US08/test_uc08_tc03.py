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


class Test_uc08_tc03:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-contact-form/1")
        self.driver.maximize_window()
        sleep(2)
    ##Gerekli değişiklikler yapılır.
    def test_contactmediumupdatepozitivetest(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")               
        email.clear()
        email.send_keys("cgronw1@imgur.com") 
        emailvalue = email.get_attribute("value")
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        homephone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
        homephone.clear()
        homephone.send_keys("3911516867")
        homevalue = homephone.get_attribute("value")
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")               
        fax.clear()
        fax.send_keys("4243253275")
        faxvalue = fax.get_attribute("value")
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               
        mphone.clear()
        mphone.send_keys("1395040000")
        mphonevalue = mphone.get_attribute("value")
        sleep(1)

        assert emailvalue == ("cgronw1@imgur.com")
        assert homevalue == ("3911516867")
        assert faxvalue == ("4243253275")
        assert mphonevalue == ("1395040000")
        

        #Save Butonuna basılır.
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")))
        savebutton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[2]/div/div[2]/button")               
        savebutton.click()
        sleep(3)

        #Değiştirilen değerler birbiri ile tutuyor mu karşılaştırılır.

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[2]/label")))
        emailcheck=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[2]/label")               
        emailcheckvalue = emailcheck.text
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[4]/label")))
        homecheck=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[4]/label")               
        homecheckvalue = homecheck.text

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[4]/label")))
        faxcheck=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[4]/label")               
        faxcheckvalue = faxcheck.text
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[2]/label")))
        mobilecheck=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[2]/label")               
        mphonechechvalue = mobilecheck.text
        
        assert emailcheckvalue == ("cgronw1@imgur.com")
        assert homecheckvalue == ("3911516867")
        assert faxcheckvalue == ("4243253275")
        assert mphonechechvalue == ("1395040000")
   
    def teardown_method(self):
        self.driver.quit()
    