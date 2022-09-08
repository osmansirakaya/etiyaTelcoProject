from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import contants_us05

class Test_tc05:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard")
        self.driver.maximize_window()
        sleep(2)

    def test_tc06 (self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")))
        customerInfoBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")
        customerInfoBtn.click()
        sleep(1)
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[3]/div/div[1]/button")))
        cancelBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[3]/div/div[1]/button")
        cancelBtn.click()

        sleep(1)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[1]/h3")))
        searchCustomerText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[1]/h3")
        assert searchCustomerText.text==contants_us05.text["searchCustomer"]
       
    def teardown_method(self):
        self.driver.quit()       