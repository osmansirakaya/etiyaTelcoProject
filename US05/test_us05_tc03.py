from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import contants_us05

### US05-TC03 Yeni Müsteri Oluşturma(Add New Address Ekranında Zorunlu Alanların Boş Bırakılması) ###

class Test_tc05:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/dashboard/customers/list-address-info")
        self.driver.maximize_window()

    @pytest.mark.parametrize("houseFlat,street,description",[("2","","6128 Alley"),("","","")])
    
    def test_tc03(self,houseFlat,street,description):
        sleep(2)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[3]/button")))
        addNewAddressBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/app-list-address-info/div/app-main-layout/div/div/div/div[3]/button")
        addNewAddressBtn.click()
    
     
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='gender']")))
        selectCity=self.driver.find_element(By.XPATH,"//*[@id='gender']")
        selectCity.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='gender']/option[2]")))
        newYorkCity=self.driver.find_element(By.XPATH,"//*[@id='gender']/option[2]")
        newYorkCity.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input")))
        houseFlatNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[2]/div/div[2]/input")
        houseFlatNumberTextBox.send_keys(houseFlat)

        sleep(2)

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[3]/div/div[2]/input")))
        streetTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[3]/div/div[2]/input")
        streetTextBox.send_keys(street)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[3]/div/div[2]/input")))
        descriptionTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[1]/div[4]/div/div[2]/textarea")
        descriptionTextBox.send_keys(description)

        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[2]/div[2]/button")))
        saveBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/app-add-address-info/div/app-main-layout/div/div/div/div[2]/div/form/div[2]/div[2]/button")
        
        sleep(2)
        
        saveBtn.click()
        sleep(3)
 
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='lastName-help']")
        sleep(3)
        assert errorMessage.text==contants_us05.error["addressMessage"]
        sleep(1)

    def teardown_method(self):
        self.driver.quit()   

