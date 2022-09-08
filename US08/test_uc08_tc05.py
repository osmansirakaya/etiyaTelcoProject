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

#contact Medium ekranı max character
class Test_uc08_tc05:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-contact-form/1")
        self.driver.maximize_window()
        sleep(2)
    #Email alanı max karakter
    def test_contactmediumupdatemaxemail(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")               
        email.clear()
        email.send_keys("kaganulupinarkaganulupinarkaganulupinarkaganulupinarkaganulupinarkaganulupinarkaganulupinar@gmail.com")
        emailcheck=email.get_attribute("value")
        assert emailcheck == ("kaganulupinarkaganulupinarkaganulupinarkaganulupinarkaganulupinarkaganulupinarkaganulupinar@gmail.com")
    #Home Phone alanı max karakter ve harf alma durumu
    def test_contactmediumupdatemaxhphone(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        hphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
        hphone.clear()
        hphone.send_keys("031228223331")
        hphonecheck=hphone.get_attribute("value")
        assert hphonecheck == ("03122822333")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        hphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
        hphone.clear()
        hphone.send_keys("0312282233a")
        hphonecheck=hphone.get_attribute("value")
        assert hphonecheck == ("0312282233")

    #Mobile Phone alanı max karakter ve harf alma durumu
    def test_contactmediumupdatemaxmphone(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               
        mphone.clear()
        mphone.send_keys("53565597611")
        mphonecheck=mphone.get_attribute("value")
        assert mphonecheck == ("5356559761")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               
        mphone.clear()
        mphone.send_keys("535655976a")
        mphonecheck=mphone.get_attribute("value")
        assert mphonecheck == ("535655976")

    #Fax alanı max karakter ve harf alma durumu
    def test_contactmediumupdatemaxfax(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")               
        fax.clear()
        fax.send_keys("90312232322222")
        faxcheck=fax.get_attribute("value")
        assert faxcheck == ("9031223232222")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")               
        fax.clear()
        fax.send_keys("903122323222a")
        faxcheck=fax.get_attribute("value")
        assert faxcheck == ("903122323222")

    def teardown_method(self):
        self.driver.quit()

    









