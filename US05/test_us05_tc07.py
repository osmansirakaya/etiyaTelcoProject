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
    
    def test_tc07(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")))
        customerInfoBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")
        customerInfoBtn.click()
        sleep(1)

    def teardown_method(self):
        self.driver.quit()         