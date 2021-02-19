import time

from selenium import webdriver
import unittest
from Test.TestLogin.Pages.loginPage import LoginPage
from Test.TestLogin.Pages.employeePage import EmployeePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()

    def test_Login_Success_with_Valid_Email_Password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_Username_Password("admin@gmail.com","123456")
        login.press_Login_button()
        driver.implicitly_wait(10)
        employee = EmployeePage(driver)
        self.assertEqual(driver.find_element_by_xpath(employee.btn_CreateEmployee).is_displayed(), True)

    def test_Login_Success_With_Valid_UppercaseEmail_and_Password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_Username_Password("ADMIN@GMAIL.COM", "123456")
        login.press_Login_button()
        driver.implicitly_wait(10)
        employee = EmployeePage(driver)
        self.assertEqual(driver.find_element_by_xpath(employee.btn_CreateEmployee).is_displayed(), True)

    def test_Login_Failed_With_Invalid_Email(self):
        driver = self.driver
        login = LoginPage(driver)

        # Data 1: Input blank spaces into Email textbox
        login.enter_Username_Password("       ", "123456")
        login.press_Login_button()
        self.assertEqual(driver.find_element_by_xpath(login.error_msg).is_displayed(), True)
        self.assertEqual(driver.find_element_by_xpath(login.btn_Login).is_enabled(), False)

        # Data 2: Input wrong email format
        driver.refresh()
        login.enter_Username_Password("minh", "123456")
        login.press_Login_button()
        self.assertEqual(driver.find_element_by_xpath(login.error_msg).is_displayed(), True)
        self.assertEqual(driver.find_element_by_xpath(login.btn_Login).is_enabled(), False)

        # Data 3: Input wrong email
        driver.refresh()
        login.enter_Username_Password("admin2@gmail.com", "123456")
        login.press_Login_button()
        driver.implicitly_wait(10)
        self.assertEqual(driver.find_element_by_xpath(login.error_msg2).is_displayed(), True)

        # Data 4: Input wrong password
        driver.refresh()
        login.enter_Username_Password("admin@gmail.com", "1234567")
        login.press_Login_button()
        driver.implicitly_wait(10)
        self.assertEqual(driver.find_element_by_xpath(login.error_msg2).is_displayed(), True)

    @classmethod
    def tearDown(self):
        self.driver.quit()
