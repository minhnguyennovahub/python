import time
import unittest
from selenium import webdriver

from Test.TestLogin.Commons.commons import MinhCommons
from Test.TestLogin.Pages.editEmployeePage import EditEmployeePage
from Test.TestLogin.Pages.employeePage import EmployeePage
from Test.TestLogin.Pages.loginPage import LoginPage


class ActionOfEmployeeTest(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enter_Username_Password("admin@gmail.com", "123456")
        self.login.press_Login_button()
        self.driver.implicitly_wait(10)

    # User is able to change status of user
    def test_TC_AEP_02(self):
        # Data 1: Deactivate an "Active" user
        driver = self.driver
        employee = EmployeePage(driver)
        employee.choose_Status(employee.opt_Active)
        time.sleep(1)
        employee.deactivate_Employee(1)
        self.assertEqual(driver.find_element_by_xpath(employee.msg_Deactivate_success).is_displayed(), True)

        # # Data 2: Activate a "Former" user
        # driver.refresh()
        # employee.choose_Status(employee.opt_Former)
        # employee.activate_Employee(1)
        # self.assertEqual(driver.find_element_by_xpath(employee.msg_Activate_success).is_displayed(), True)

    def test_TC_AEP_03(self):
        driver = self.driver
        employee = EmployeePage(driver)
        editEmployee = EditEmployeePage(driver)
        employee.click_Edit_button(1)
        self.assertEqual(driver.current_url, editEmployee.editPage_url)

    def test_TC_AEP_07(self):
        driver = self.driver
        employee = EmployeePage(driver)
        editEmployee = EditEmployeePage(driver)
        common = MinhCommons(driver)

        # Data 1: Test with all text fields are minimum of characters
        employee.click_Edit_button(2)
        time.sleep(2)
        editEmployee.edit_profile("ab", "ba", common.random_string(10)+"@gmail.com", "040401997", "0899875463", "01112021")
        editEmployee.click_save_button()
        common.wait_displayed(editEmployee.msg_edit_success)
        check = driver.find_element_by_xpath(editEmployee.msg_edit_success).is_displayed()

        #Data 2: Test with all text fields are maximum of characters
        employee.click_Edit_button(2)
        time.sleep(2)
        editEmployee.edit_profile("nguyennguyennguyenng", "nguyennguyennguyenng", common.random_string(64) + "@gmail.com", "040401997", "0899875464",
                                  "01112021")
        editEmployee.click_save_button()
        common.wait_displayed(editEmployee.msg_edit_success)

        check2 = driver.find_element_by_xpath(editEmployee.msg_edit_success).is_displayed()

        self.assertEqual(check, True)
        self.assertEqual(check2, True)
    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print("done")