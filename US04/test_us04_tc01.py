from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


### US04-TC01- Müşteri Arama ve Görüntüleme Sayfasında Form Elemanlarının Görünürlüğü ###
class Test_tc01:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/customer-dashboard")
        self.driver.maximize_window()
        sleep(2)
        
    def test_tc01(self):
        #Create Customer
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")))
        createCustomerBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/button")
        assert createCustomerBtn.is_displayed

        #natID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[1]")))
        natIdNumberText= self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[1]")
        assert natIdNumberText.is_displayed                
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[1]")))
        natIdNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[1]")
        assert natIdNumberTextBox.is_displayed                
        natIdNumberTextBox.click()

        #custID
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[2]")))
        custIdText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[2]")
        assert custIdText.is_displayed
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[2]")))
        custIdTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[2]")
        assert custIdTextBox.is_displayed
        custIdTextBox.click()

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        
        #accountNumber
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[3]")))
        accountNumberText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[3]")
        assert accountNumberText.is_displayed
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[3]")))
        accountNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[3]")
        
        actions.send_keys(Keys.PAGE_DOWN).perform()
        assert accountNumberTextBox.is_displayed
        accountNumberTextBox.click()
        
        #gsmNumber
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[4]")))
        gsmNumberText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[4]")
        assert gsmNumberText.is_displayed
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[4]")))
        gsmNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[4]")
        assert gsmNumberTextBox.is_displayed
        gsmNumberTextBox.click()
        
        actions.send_keys(Keys.PAGE_DOWN).perform()
        
        #firstName
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[5]")))
        firstNameText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[5]")
        assert firstNameText.is_displayed
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")))
        firstNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")
        assert  firstNameTextBox.is_displayed
        firstNameTextBox.click()

        #lastName
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[6]")))
        lastNameText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[6]")
        assert lastNameText.is_displayed
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[6]")))
        lastNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[6]")
        assert  lastNameTextBox.is_displayed
        lastNameTextBox.click()
 
        #orderNumber
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[7]")))
        orderNumberText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/label[7]")
        assert orderNumberText.is_displayed
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[7]")))
        orderNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[7]")
        assert  orderNumberTextBox.is_displayed
        orderNumberTextBox.click()

        #searchBtn    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2][@disabled]")))
        searchBtn = self.driver.find_elements(By.XPATH, "/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[2][@disabled]")
        assert len(searchBtn) > 0

        #clearBtn
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[1]")))
        clearBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[3]/button[1]")
        assert clearBtn.is_displayed

        #customerTable
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div")))
        customerTable=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div")
        assert customerTable.is_displayed

    def teardown_method(self):
        self.driver.quit()    


