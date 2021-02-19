import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.TestLogin.Pages.employeePage import EmployeePage
from Test.TestLogin.Pages.loginPage import LoginPage


class FilterByStatus(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enter_Username_Password("admin@gmail.com", "123456")
        self.login.press_Login_button()
        self.driver.implicitly_wait(10)

    # All employees are displayed when Filter is All
    def test_TC_FS_01(self):
        driver = self.driver
        employee = EmployeePage(driver)
        employee.choose_Status(employee.opt_All)
        rows = driver.find_elements_by_xpath("//tbody/tr")
        self.assertEqual(len(rows), 9)

    # The result displays matching with Status has chosen
    def test_TC_FS_02(self):
        driver = self.driver
        employee = EmployeePage(driver)

        # Data 1: Filter by Active
        employee.choose_Status(employee.opt_Active)
        rows = driver.find_elements_by_xpath("//tbody/tr")

        # Data 2: Filter by Former
        employee.choose_Status(employee.opt_Former)
        time.sleep(2)
        rows1 = driver.find_elements_by_xpath("//tbody/tr")

        self.assertEqual(len(rows), 6)
        self.assertEqual(len(rows1), 3)

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print("done")