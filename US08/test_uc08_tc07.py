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


class Test_uc08_tc07:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-contact-medium/1")
        self.driver.maximize_window()
        sleep(2)
    
    
    ##Contact Medium Güncelleme ekranında düzenlenen alanlar Save seçeneğine tıklandıktan sonra Contact Medium 
    # sayfasındaki veriler ile aynı olmalıdır.

    
    def test_datacheck(self):       
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[2]/label")))
        email=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[2]/label")               
        emailkontrol = email.text

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[4]/label")))
        homephone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[1]/div[4]/label")               
        homephonekontrol = homephone.text

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[4]/label")))
        fax=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[4]/label")               
        faxkontrol = fax.text

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[2]/label")))
        mphone=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/div[2]/div[2]/label")               
        mphonekontrol = mphone.text
   
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/button[2]")))
        clictedit=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/button[2]")               
        clictedit.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")))
        email2=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[1]/div/input")               
        value=email2.get_attribute("value")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")))
        homephone2=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[2]/div/input")               
        homevalue=homephone2.get_attribute("value")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")))
        faxkontrol2=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[4]/div/input")               
        faxvalue=faxkontrol2.get_attribute("value")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")))
        mphonekontrol2=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div[2]/div/form/div[1]/div/div[3]/div/input")               
        mphonevalue=mphonekontrol2.get_attribute("value")


        assert value==emailkontrol
        assert homevalue==homephonekontrol
        assert faxvalue==faxkontrol
        assert mphonevalue==mphonekontrol


    def teardown_method(self):
        self.driver.quit()





        

        
