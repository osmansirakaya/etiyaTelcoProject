from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_tc03:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/login")
        self.driver.maximize_window()
        sleep(3)
        
    def test_tc03(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[1]/input")))
        usernameBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[1]/input")
        usernameBox.send_keys("admin")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[2]/input")))
        passwordBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/div[2]/input")
        passwordBox.send_keys("admin")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/button")))
        loginBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div[2]/div/div[2]/form/div/button")
        loginBtn.click()
        sleep(3)
        welcomeText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/div/app-user-info/div/div[1]")
        actualText=welcomeText.text
        exceptedText="WELCOME ROSE!" 
        assert actualText==exceptedText

    def teardown_method(self):
        self.driver.quit()    
