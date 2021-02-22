import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    # Edit Employees Profile page displays after clicking on Edit Profile button
    def test_TC_AEP_06(self):
        driver = self.driver
        employee = EmployeePage(driver)
        editEmployee = EditEmployeePage(driver)
        employee.click_Edit_button(1)
        self.assertEqual(driver.current_url, editEmployee.editPage_url)

    # Edited successful after inputting all valid data into all fields
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

    # "First name" field allows from 2 to 20 characters
    def test_TC_AEP_08(self):
        driver = self.driver
        employee = EmployeePage(driver)
        editEmployee = EditEmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        driver.find_element_by_xpath(editEmployee.txt_Email).clear()
        driver.find_element_by_xpath(editEmployee.txt_Firstname).clear()
        driver.find_element_by_xpath(editEmployee.txt_Phone).send_keys(Keys.TAB)

        check = driver.find_element_by_xpath(editEmployee.msg_firstname_required).is_displayed()
        check1 = driver.find_element_by_xpath(editEmployee.msg_email_required).is_displayed()
        self.assertEqual(check, True) and self.assertEqual(check1, True)

    # "First name" field allows from 2 to 20 characters
    def test_TC_AEP_09(self):
        driver = self.driver
        employee = EmployeePage(driver)
        editEmployee = EditEmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)

        # Data 1: Input 1 character into First name field
        driver.find_element_by_xpath(editEmployee.txt_Firstname).clear()
        driver.find_element_by_xpath(editEmployee.txt_Firstname).send_keys("m")
        check = driver.find_element_by_xpath("//div[@class='invalid-feedback']/div[contains(.,' Fi')]").is_displayed()
        check1 = driver.find_element_by_xpath(editEmployee.btn_Save).is_enabled()

        # Data 2: Input 21 characters into First name field
        driver.find_element_by_xpath(editEmployee.txt_Firstname).send_keys("mmmmmmmmmmmmmmmmmmmm")
        check2 = driver.find_element_by_xpath("//div[@class='invalid-feedback']/div[contains(.,' First name must not exceed 20 characters ')]").is_displayed()

        self.assertEqual(check, True) and self.assertEqual(check1, False)
        self.assertEqual(check2, True)

    # "Last name" field allows from 2 to 20 characters
    def test_TC_AEP_10(self):
        driver = self.driver
        employee = EmployeePage(driver)
        editEmployee = EditEmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)

        # Data 1: Input 1 character into Last name field
        driver.find_element_by_xpath(editEmployee.txt_Lastname).clear()
        driver.find_element_by_xpath(editEmployee.txt_Lastname).send_keys("m")
        check = driver.find_element_by_xpath("//div[@class='invalid-feedback']/div[contains(.,' La')]").is_displayed()
        check1 = driver.find_element_by_xpath(editEmployee.btn_Save).is_enabled()

        # Data 2: Input 21 characters into Last name field
        driver.find_element_by_xpath(editEmployee.txt_Lastname).send_keys("mmmmmmmmmmmmmmmmmmmm")
        check2 = driver.find_element_by_xpath("//div[@class='invalid-feedback']/div[contains(.,' Last name must not exceed 20 characters ')]").is_displayed()

        self.assertEqual(check, True) and self.assertEqual(check1, False)
        self.assertEqual(check2, True)

    # Cannot edit profile when inputting into "Firstname/Lastname" field blank spaces only
    def test_TC_AEP_11(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)

        driver.find_element_by_xpath(editEmployee.txt_Firstname).clear()
        driver.find_element_by_xpath(editEmployee.txt_Firstname).send_keys(Keys.SPACE * 10)
        driver.find_element_by_xpath(editEmployee.txt_Lastname).clear()
        driver.find_element_by_xpath(editEmployee.txt_Lastname).send_keys(Keys.SPACE * 10)

        check = driver.find_element_by_xpath(editEmployee.btn_Save).is_enabled()
        self.assertEqual(check, False)

    # Cannot edit profile when inputting invalid email format
    def test_TC_AEP_12(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        driver.find_element_by_xpath(editEmployee.txt_Email).clear()
        driver.find_element_by_xpath(editEmployee.txt_Email).send_keys("ndminh4497@@gmail.com")

        check = driver.find_element_by_xpath(editEmployee.msg_email_required).is_displayed()
        self.assertEqual(check, True)

    # Validation message is displayed when inputting a signed up email
    def test_TC_AEP_13(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        common = MinhCommons(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        common.copy_text(editEmployee.txt_Email)
        driver.back()
        employee.click_Edit_button(3)
        time.sleep(2)
        driver.find_element_by_xpath(editEmployee.txt_Email).clear()
        common.paste_text(editEmployee.txt_Email)
        editEmployee.click_save_button()
        check = driver.find_element_by_xpath(editEmployee.msg_email_required).is_displayed()
        self.assertEqual(check, True)

    # Edit profile failed when inputting birthday field more than current date
    def test_TC_AEP_14(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        driver.find_element_by_xpath(editEmployee.txt_Birthday).send_keys("01112030")
        driver.find_element_by_xpath(editEmployee.txt_Birthday).send_keys(Keys.TAB)
        check = driver.find_element_by_xpath(editEmployee.msg_error_birthday).is_displayed()
        self.assertEqual(check, True)

    # "Phone Number" only accepts number characters
    def test_TC_AEP_16(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        check = driver.find_element_by_xpath(editEmployee.txt_Phone).get_attribute('value')
        driver.find_element_by_xpath(editEmployee.txt_Phone).send_keys("!@#$%^&*")
        check1 = driver.find_element_by_xpath(editEmployee.txt_Phone).get_attribute('value')
        self.assertEqual(check, check1)

    # Phone number requires from 10 to 12 digits
    def test_TC_AEP_17(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        driver.find_element_by_xpath(editEmployee.txt_Phone).clear()
        driver.find_element_by_xpath(editEmployee.txt_Phone).send_keys("1" * 9)
        driver.find_element_by_xpath(editEmployee.txt_Phone).send_keys(Keys.TAB)
        check = driver.find_element_by_xpath(editEmployee.msg_error_phone).is_displayed()
        driver.find_element_by_xpath(editEmployee.txt_Phone).send_keys("1" * 4)
        driver.find_element_by_xpath(editEmployee.txt_Phone).send_keys(Keys.TAB)
        check1 = driver.find_element_by_xpath(editEmployee.msg_error_phone).is_displayed()
        self.assertEqual(check, True)
        self.assertEqual(check1, True)

    # Cannot edit profile when inputting into Join date field more than current date
    def test_TC_AEP_18(self):
        driver = self.driver
        editEmployee = EditEmployeePage(driver)
        employee = EmployeePage(driver)
        employee.click_Edit_button(2)
        time.sleep(2)
        driver.find_element_by_xpath(editEmployee.txt_Joindate).send_keys("01112030")
        driver.find_element_by_xpath(editEmployee.btn_Save).click()
        check = driver.find_element_by_xpath(editEmployee.msg_error_birthday).is_displayed()
        self.assertEqual(check, True)

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
        print("done")