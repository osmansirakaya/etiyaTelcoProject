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

class Test_tc04:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/customer-dashboard")
        self.driver.maximize_window() 
        sleep(2)

    # girilen nationalityId ile arama yapılır ve listedeki nationalityId ile eşleme durumu kontrol edilir.
    @pytest.mark.parametrize("nationalityId",[("49733447980")])
    def test_nationalityId(self,nationalityId): 

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[1]")))
        nIdTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[1]")
        nIdTextBox.send_keys(nationalityId)
        value=nIdTextBox.get_attribute("value")
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()      
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")))
        clickSearch=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")    
        sleep(3)           
        clickSearch.click()

        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/td[5]")))
        naIdText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/td[5]")               
        naIdKontrol = naIdText.text

        assert value==naIdKontrol
      
    def teardown_method(self):
        self.driver.quit()

    # girilen customerId ile arama yapılır ve listedeki customerId ile eşleme durumu kontrol edilir.
    @pytest.mark.parametrize("customerId",[("7")])
    def test_customerId(self,customerId): 

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[2]")))
        customerIdTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[2]")
        customerIdTextBox.send_keys(customerId)
        value=customerIdTextBox.get_attribute("value")
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()      
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")))
        clickSearch=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")    
        sleep(3)           
        clickSearch.click()

        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(2)
     
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        cIdText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")               
        customerIdKontrol = cIdText.text

        assert value==customerIdKontrol
      
    def teardown_method(self):
        self.driver.quit()

    # girilen firstName ile arama yapılır ve listedeki firstName ile eşleme durumu kontrol edilir.
    @pytest.mark.parametrize("firstName",[("Edward")])
    def test_firstName(self,firstName): 

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")))
        firstNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")
        firstNameTextBox.send_keys(firstName)
        value=firstNameTextBox.get_attribute("value")
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()      
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")))
        clickSearch=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")    
        sleep(3)           
        clickSearch.click()

        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(2)
     
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/td[1]")))
        nameText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/td[1]")               
        firstNamedKontrol = nameText.text

        assert value==firstNamedKontrol
      
    def teardown_method(self):
        self.driver.quit()

    # girilen lastName ile arama yapılır ve listedeki lastName ile eşleme durumu kontrol edilir.
    @pytest.mark.parametrize("lastName",[("Creavan")])
    def test_lastName(self,lastName): 
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[6]")))
        lastNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[6]")
        lastNameTextBox.send_keys(lastName)
        value=lastNameTextBox.get_attribute("value")
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()      
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")))
        clickSearch=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2]")    
        sleep(3)           
        clickSearch.click()

        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(2)
     
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/td[3]")))
        lastnameText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/td[3]")               
        firstNamedKontrol = lastnameText.text

        assert value==firstNamedKontrol
      
    def teardown_method(self):
        self.driver.quit()