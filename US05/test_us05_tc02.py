from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from argparse import Action
from selenium.webdriver.common.action_chains import ActionChains 
import contants_us05


### US05-TC02- Yeni Müsteri Oluşturma (Demografik Bilgiler Ekranında Zorunlu Alanların 
# Boş Bırakılması)###
 
class Test_tc02:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/customer-dashboard")
        self.driver.maximize_window()
        sleep(2)

    @pytest.mark.parametrize("firstName,lastName,middleName,birthDate,fatherName,motherName,nationalityId",
     [("Betul", "Yesiloglu", "Gunes","11/11/1999","Ahmet","Ayşe","11111111119" )])
    def test_createCustomer(self,firstName,lastName,middleName,birthDate,fatherName,motherName,nationalityId):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")))
        createCustomerBtn=self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")
        createCustomerBtn.click()
        sleep(2) 

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[1]/div/div[2]/input")))
        firstNameTextBox= self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[1]/div/div[2]/input") 
        firstNameTextBox.send_keys(firstName) 
        sleep(2)
        
        lastNameTextBox= self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[3]/div/div[2]/input")
        lastNameTextBox.send_keys(lastName) 
        
        middleNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[2]/div/div[2]/input")
        middleNameTextBox.send_keys(middleName) 
        sleep(1)

        birthDateTextBox =self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[4]/div/div[2]/input")
        birthDateTextBox.click()
        sleep(2)
        birthDateTextBox.send_keys(birthDate)  

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        sleep(2)

        fatherNameTextBox=self.driver.find_element(By.XPATH, "/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[6]/div/div[2]/input")
        fatherNameTextBox.send_keys(fatherName)   

        motherNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[7]/div/div[2]/input")
        motherNameTextBox.send_keys(motherName) 

        nationalityIdTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[2]/form/div/div[8]/div/div[2]/input")
        nationalityIdTextBox.send_keys(nationalityId) 

        nextBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/app-main-layout/div/div/div/div[3]/div/div[2]/button")
        nextBtn.click() 
        
        errorMessage=self.driver.find_element(By.XPATH,"//*[@class='p-error block ng-invalid ng-dirty ng-star-inserted']")
        assert errorMessage.text== contants_us05.error["demographicInfo"] 

        sleep(3)

    def teardown_method(self):
       self.driver.quit()    