import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Test.TestLogin.Commons.commons import MinhCommons
from Test.TestLogin.Pages.createEmployeePage import CreateEmployeePage
from Test.TestLogin.Pages.employeePage import EmployeePage
from Test.TestLogin.Pages.loginPage import LoginPage


class CreateEmployeeTest(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enter_Username_Password("admin@gmail.com", "123456")
        self.login.press_Login_button()
        self.driver.implicitly_wait(10)

    # Create employee profile successful with all valid data
    def test_TC_CEP_02(self):

        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        employee.click_create_button()

        # Test with minimum digits of First name and Last name
        create = CreateEmployeePage(driver)
        create.create_profile("abc", "ba", common.random_string(3)+"@gmail.com", "ducminh123", "ducminh123", "04041997",
                              "0899875463", "01112021")
        create.click_save_button()
        common.wait_displayed(create.msg_create_success)
        check = driver.find_element_by_xpath(create.msg_create_success).is_displayed()
        self.assertEqual(True, check)
        # Test with maximum digits of Firstname Last name and Email localpart
        employee.click_create_button()
        create.create_profile("nguyennguyennguyenng", "nguyennguyennguyenng", common.random_string(64) + "@gmail.com", "ducminh123"
                              , "ducminh123", "04041997", "0899875463", "01112023")
        create.click_save_button()
        common.wait_displayed(create.msg_create_success)
        self.assertEqual(True, check)

    # All fields of General Information are required to create employee profile
    def test_CEP_03(self):
        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        create = CreateEmployeePage(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        employee.click_create_button()
        create.create_profile("", "", "", "", "", "", "", "")
        driver.find_element(By.XPATH, "//input[@type='number']").clear()
        driver.find_element(By.XPATH, create.txt_Phone).click()
        check = driver.find_element(By.XPATH, create.msg_firstname_required).is_displayed()
        check1 = driver.find_element(By.XPATH, create.msg_error_phone).is_displayed()
        self.assertEqual(True, check)
        self.assertEqual(True, check1)

    def test_CEP_04(self):
        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        create = CreateEmployeePage(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        employee.click_create_button()

        # Test with First name is 1 character
        driver.find_element(By.XPATH, create.txt_Firstname).send_keys("m")
        driver.find_element(By.XPATH, create.txt_Firstname).send_keys(Keys.TAB)
        check = driver.find_element(By.XPATH, create.msg_firstname_required).is_displayed()
        self.assertEqual(True, check)

        # Test with First name is 21 characters
        driver.find_element(By.XPATH, create.txt_Firstname).send_keys(common.random_string(20))
        driver.find_element(By.XPATH, create.txt_Firstname).send_keys(Keys.TAB)
        check1 = driver.find_element(By.XPATH, create.msg_firstname_required).is_displayed()
        self.assertEqual(True, check1)

    # "Last name" field requires 2 to 20 characters
    def test_CEP_05(self):
        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        create = CreateEmployeePage(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        employee.click_create_button()

        # Test with Last name is 1 characters
        driver.find_element(By.XPATH, create.txt_Lastname).send_keys("m")
        driver.find_element(By.XPATH, create.txt_Lastname).send_keys(Keys.TAB)
        check = driver.find_element(By.XPATH, create.msg_lastname_required).is_displayed()
        self.assertEqual(True, check)

        # Test with Last name is 21 characters
        driver.find_element(By.XPATH, create.txt_Lastname).send_keys(common.random_string(20))
        driver.find_element(By.XPATH, create.txt_Lastname).send_keys(Keys.TAB)
        check1 = driver.find_element(By.XPATH, create.msg_lastname_required).is_displayed()
        self.assertEqual(True, check1)

    # Create profile failed when inputting only blank spaces into "Firstname/Lastname" field
    def test_CEP_06(self):
        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        create = CreateEmployeePage(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        employee.click_create_button()
        driver.find_element(By.XPATH, create.txt_Firstname).send_keys(Keys.SPACE * 10)
        create.create_profile("          ", "          ", common.random_string(10)+"@gmail.com", "ducminh123", "ducminh123"
                              , "04041997", "0899875463","01112021")
        create.click_save_button()
        check_first_name = driver.find_element(By.XPATH, create.msg_firstname_required).is_displayed()
        check_last_name = driver.find_element(By.XPATH, create.msg_lastname_required).is_displayed()
        self.assertEqual(True, check_first_name)
        self.assertEqual(True, check_last_name)
        self.assertEqual(create.url, driver.current_url)

    # Create profile failed when inputting invalid email format
    def test_CEP_07(self):
        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        create = CreateEmployeePage(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        employee.click_create_button()

        # Test with "@@" between local part and domain
        create.create_profile("Minh", "Nguyen", common.random_string(5)+"@@gmail.com", "ducminh123", "ducminh123", "04041997", "0899875463", "01112021")
        create.click_save_button()
        check = driver.find_element(By.XPATH, create.msg_error_email).is_displayed()
        self.assertEqual(True, check)

        # Test with invalid domain
        driver.find_element(By.XPATH, create.txt_Email).clear()
        driver.find_element(By.XPATH, create.txt_Email).send_keys(common.random_string(10) + "@gmail")
        create.click_save_button()
        self.assertEqual(create.url, driver.current_url)

        # Test with Local part is 65 characters
        driver.find_element(By.XPATH, create.txt_Email).clear()
        driver.find_element(By.XPATH, create.txt_Email).send_keys(common.random_string(65)+"@gmail.com")
        create.click_save_button()
        check1 = driver.find_element(By.XPATH, create.msg_error_email).is_displayed()
        self.assertEqual(True, check1)

        # Test with email is contains special characters
        driver.find_element(By.XPATH, create.txt_Email).clear()
        driver.find_element(By.XPATH, create.txt_Email).send_keys("user_3!@#$%^@gmail.com")
        create.click_save_button()
        check2 = driver.find_element(By.XPATH, create.msg_error_email).is_displayed()
        self.assertEqual(True, check2)

    def test_TC_CEP_08(self):
        driver = self.driver
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        create = CreateEmployeePage(driver)
        common.wait_displayed(employee.btn_CreateEmployee)
        check = create.get_email(4)
        employee.click_create_button()
        create.create_profile("minh", "nguyen", check, "ducminh123", "ducminh123", "04041997", "0899875463", "01112021")
        create.click_save_button()
        self.assertEqual(create.url, driver.current_url)

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print("done")
