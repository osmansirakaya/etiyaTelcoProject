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
        self.driver.get("http://localhost:4200/dashboard/customers/contact-medium")
        self.driver.maximize_window()
        sleep(2)

    # girdi alanlarından mobilePhone boş bırakılarak create işlemi yapılır. Boş bırakılan alanın hata mesajı kontrol edilir.
    @pytest.mark.parametrize("email,mPhone,hPhone,fax",[("osmansirakaya96@gmail.com","","03122222222","03122324444"),("","05555555555","03122222222","03122324444")])
    def test_contactMedium_err(self,email,mPhone,hPhone,fax):

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[1]/div/div[2]/input")))
        emailTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[1]/div/div[2]/input")
        emailTextBox.send_keys(email)
        sleep(1)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[2]/div/div[2]/input")))
        hPhoneTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[2]/div/div[2]/input")
        hPhoneTextBox.send_keys(hPhone)
        sleep(1)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[3]/div/div[2]/input")))
        mPoneTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[3]/div/div[2]/input")
        mPoneTextBox.send_keys(mPhone)
        sleep(1)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[4]/div/div[2]/input")))
        faxTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[1]/div[4]/div/div[2]/input")
        faxTextBox.send_keys(fax)
        sleep(1)

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[2]/div/button")))
        clickCreate=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-contact-medium/div/app-main-layout/div/div/div/div[2]/form/div[2]/div/button")    
        sleep(1)
        clickCreate.click()     
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@class='p-error block ng-invalid ng-dirty ng-star-inserted']")))
        errorText=self.driver.find_element(By.XPATH,"//*[@class='p-error block ng-invalid ng-dirty ng-star-inserted']")
        assert errorText.text==contants_us05.error["contactMediumMessage"]
        sleep(1)

    def teardown_method(self):
        self.driver.quit()