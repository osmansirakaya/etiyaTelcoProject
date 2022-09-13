import constants_us04
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import constants_us04

### US04-TC05- Müşteri Arama ve Görüntüleme (Customer Info Sayfasına Ulaşılması) ###

class Test_tc05:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:4200/customer-dashboard")
        self.driver.maximize_window()
        sleep(2)

    @pytest.mark.parametrize("idNumber",[("67712315360")])
    def test_iDNumber(self,idNumber):       
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[1]")))
        natIdNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[1]")               
        natIdNumberTextBox.send_keys(idNumber)
        sleep(3)
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
        searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")
        sleep(3)
        
        searchBtn.click()
        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(3)
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
        customerIdBtn.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
        customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
        assert customerInfoText.text==constants_us04.customer["info"]

        
    
    @pytest.mark.parametrize("custId",[("3")])
    def test_customerID(self,custId):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[2]")))
        custIdTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[2]")
        custIdTextBox.send_keys(custId)
        sleep(3)
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
        searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")
    
        sleep(3)
        searchBtn.click()
        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
        customerIdBtn.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
        customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
        assert customerInfoText.text==constants_us04.customer["info"]

   
    
    @pytest.mark.parametrize("accountNumber",[("6531612924")])
    def test_accountNumber(self,accountNumber):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[3]")))
        accountNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[3]")         
        accountNumberTextBox.send_keys(accountNumber)
        sleep(3)
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
        searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")
        
        sleep(3)
        searchBtn.click()
        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
        customerIdBtn.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
        customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
        assert customerInfoText.text==constants_us04.customer["info"]

    @pytest.mark.parametrize("gsmNumber",[("300303906")])
    def test_gsmNumber(self,gsmNumber):
        
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[4]")))
        gsmNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[4]")
        gsmNumberTextBox.send_keys(gsmNumber)
        sleep(3)
        
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
        searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")
        
        sleep(3)
        searchBtn.click()
        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
        customerIdBtn.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
        customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
        assert customerInfoText.text==constants_us04.customer["info"]

       
    @pytest.mark.parametrize("firstName",[("Codee")])
    def test_firstName(self,firstName):

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")))
        firstNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[5]")
        firstNameTextBox.send_keys(firstName)
        sleep(3)
        
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
        searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")

        searchBtn.click()
        sleep(2) 
        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(3)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
        customerIdBtn.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
        customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
        assert customerInfoText.text==constants_us04.customer["info"]

               
    @pytest.mark.parametrize("lastName",[("Gartan")])
    def test_lastName(self,lastName):

        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[6]")))
        lastNameTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[6]")
        lastNameTextBox.send_keys(lastName)
        sleep(3)
        
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
        searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")
        searchBtn.click()
        sleep(3)
        
        actions.send_keys(Keys.PAGE_UP).perform()
        sleep(2)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
        customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
        customerIdBtn.click()
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
        customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
        assert customerInfoText.text==constants_us04.customer["info"]

    # @pytest.mark.parametrize("orderNumber",[("**************")])
    # def test_orderNumber(self,orderNumber):##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #     actions=ActionChains(self.driver)
    #     actions.send_keys(Keys.PAGE_DOWN)
    #     actions.perform()
        
    #     WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[7]")))
    #     orderNumberTextBox=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[1]/app-side-filter/div/div[2]/form/input[7]")
    #     orderNumberTextBox.send_keys(orderNumber)
    #     sleep(3)
        
    #     WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@etiyabutton='search']")))
    #     searchBtn=self.driver.find_element(By.XPATH,"//*[@etiyabutton='search']")
    #     searchBtn.click()
    #     sleep(3)

    #     actions.send_keys(Keys.PAGE_UP).perform()
    #     sleep(2)

    #     WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")))
    #     customerIdBtn=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/div/div/div/div[2]/div/app-container/div/div/app-table-info/div/table/tbody/tr/th/a")
    #     customerIdBtn.click()
        
    #     WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")))
    #     customerInfoText=self.driver.find_element(By.XPATH,"/html/body/app-root/ng-component/app-main-layout/div/span[3]")
    #     assert customerInfoText.text==constants_us04.customer["info"]


    def teardown_method(self):
        self.driver.quit()           