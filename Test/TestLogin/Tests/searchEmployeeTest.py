import time
import unittest
from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from Test.TestLogin.Pages.employeePage import EmployeePage
from Test.TestLogin.Pages.loginPage import LoginPage


class SearchEmployeeTest(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enter_Username_Password("admin@gmail.com", "123456")
        self.login.press_Login_button()
        self.driver.implicitly_wait(10)

    # Search result displays matching with search term
    def test_TC_EM_02(self):
        driver = self.driver
        employee = EmployeePage(driver)

        #Data 1: All lowercase
        employee.enter_Search_term("minh")
        employee.press_Search_button()
        driver.implicitly_wait(10)
        check = driver.find_element_by_xpath("//tr[1]/td[1]").text
        check2 = driver.find_element_by_xpath("//tr[2]/td[1]").text


        #Data 2: All uppercase
        employee.delete_Search_term()
        employee.enter_Search_term("MINH")
        employee.press_Search_button()
        driver.implicitly_wait(10)
        check3 = driver.find_element_by_xpath("//tr[1]/td[1]").text
        check4 = driver.find_element_by_xpath("//tr[2]/td[1]").text


        #Data 3: Phone number
        employee.delete_Search_term()
        employee.enter_Search_term("0899875465")
        employee.press_Search_button()
        driver.implicitly_wait(10)
        check5 = driver.find_element_by_xpath("//tr[1]/td[1]").text


        #Data 4: Contains space
        employee.delete_Search_term()
        employee.enter_Search_term("nguyen minh")
        employee.press_Search_button()
        time.sleep(1)
        check6 = driver.find_element_by_xpath("//tr[1]/td[1]").text


        self.assertEqual(check, "Nguyen Duc Minh")
        self.assertEqual(check2, "Nguyen Minh")
        self.assertEqual(check3, "Nguyen Duc Minh")
        self.assertEqual(check4, "Nguyen Minh")
        self.assertEqual(check5, "Nguyen Duc Minh")
        self.assertEqual(check6, "Nguyen Duc Minh")

     # Display "No result" when the search term is not matched
    def test_TC_EM_03(self):
        driver = self.driver
        employee = EmployeePage(driver)
        employee.enter_Search_term("!@#$%^")
        employee.press_Search_button()
        self.assertEqual(driver.find_element_by_xpath(employee.msg_noResult).is_displayed(), True)

    # Search is not response when Search term contains blank space only

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print("done")