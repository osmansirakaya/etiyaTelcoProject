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


class Test_uc08_tc01:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-info/1")
        self.driver.maximize_window()
        sleep(2)
    
    
    ##"Contact Medium" butonu görünür ve tıklanabilir olmalı.

    def test_navbarcontactmedium(self): 

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/div/div[1]/app-bar-menu/div/button[4]")))
        contactmediumbutton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/div/div[1]/app-bar-menu/div/button[4]")               
        contactmediumbutton.click()
        assert contactmediumbutton.is_displayed
    
    ##"Contact Medium" butonuna tıklayınca, "Contact Medium" sayfası açılmalı.
    def test_opencontactmediumopentopage(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/div/div[1]/app-bar-menu/div/button[4]")))
        contactmediumbutton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/div/div[1]/app-bar-menu/div/button[4]")               
        contactmediumbutton.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/span[3]")))
        contactmediumpage=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/span[3]")               
        expected_message = "Contact Medium"
        assert contactmediumpage.text.strip()==expected_message

    #"Contact Medium" sayfasındaki seçenekler görünür, tıklanabilir ve görünebilir olmalı.
    def test_contactmediumpage(self):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/div/div[1]/app-bar-menu/div/button[4]")))
        contactmediumbutton=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/div/div[1]/app-bar-menu/div/button[4]")               
        contactmediumbutton.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[2]/label")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[2]/label")               
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[4]/label")))
        homephone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[4]/label")               
       
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[4]/label")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[4]/label")               

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[2]/label")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[2]/label")               
    
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/button[2]")))
        editbuttondisplayed=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/button[2]")               
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/button[1]")))
        deletebuttondisplayed=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/button[1]")               
        
        
        assert email.is_displayed
        assert mphone.is_displayed
        assert homephone.is_displayed
        assert fax.is_displayed
        assert editbuttondisplayed.is_selected
        assert deletebuttondisplayed.is_selected

    def teardown_method(self):
        self.driver.quit()

        
        







    


    



      







      


