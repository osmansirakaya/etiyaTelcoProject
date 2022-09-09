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
    def test_createCustomer(self):   

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")))
        createCustomerClick = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")
        sleep(2)
        createCustomerClick .click()
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[1]/div/div[2]/input")))
        firstNameInput = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[1]/div/div[2]/input")        
        firstNameInput.send_keys("Ahmet")
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[2]/div/div[2]/input")))
        MiddleNameInput = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[2]/div/div[2]/input")        
        MiddleNameInput.send_keys("Yusuf")
        sleep(2)

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[3]/div/div[2]/input")))
        lastNameInput = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[3]/div/div[2]/input")        
        lastNameInput.send_keys("Demir")
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[4]/div/div[2]/input")))
        birthDate = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[4]/div/div[2]/input")        
        birthDate.send_keys("11/03/1999")
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[5]/div/div[2]/div/select")))
        genderClick = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[5]/div/div[2]/div/select")
        genderClick .click()
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[5]/div/div[2]/div/select/option[3]")))
        maleClick = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[5]/div/div[2]/div/select/option[3]")
        maleClick .click()
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[6]/div/div[2]/input")))
        fatherName = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[6]/div/div[2]/input")        
        fatherName.send_keys("Mustafa")
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[7]/div/div[2]/input")))
        motherName = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[7]/div/div[2]/input")        
        motherName.send_keys("Ayşe")
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located
        ((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[8]/div/div[2]/input")))
        nationalityId= self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[8]/div/div[2]/input")        
        nationalityId.send_keys("48776304564")
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[3]/div/div[2]/button")))
        nextClick = self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[3]/div/div[2]/button")
        nextClick .click()
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-custom-toast/p-toast/div/p-toastitem/div/div/div/p")))
        streetName=self.driver.find_element(By.XPATH,"/html/body/app-root/app-custom-toast/p-toast/div/p-toastitem/div/div/div/p")
        assert streetName.text == "This user already exist"
















        





    def teardown_method(self):
        self.driver.quit()

    