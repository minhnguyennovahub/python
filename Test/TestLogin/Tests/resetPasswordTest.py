import time
import unittest
from selenium import webdriver

from Test.TestLogin.Pages.loginPage import LoginPage
from Test.TestLogin.Pages.resetPasswordPage import ResetPasswordPage


class resetPasswordTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()

    def test_Reset_Password_page_is_displayed(self):
        driver = self.driver
        login = LoginPage(driver)
        resetPW = ResetPasswordPage(driver)
        login.click_Forgot_Password()
        self.assertEqual(driver.find_element_by_xpath(resetPW.txt_email).is_displayed(), True)

    # Unable to run this test case due to 2 steps verification of Gmail

    # def test_Receive_token_after_input_email(self):
    #     driver = self.driver
    #     login = LoginPage(driver)
    #     resetPW = ResetPasswordPage(driver)
    #     login.click_Forgot_Password()
    #     resetPW.enter_username("minhnguyen+1@novahub.vn")
    #     resetPW.click_next_button()
    #     driver.execute_script("window.open('');")
    #     driver.switch_to.window(driver.window_handles[1])
    #     driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    #     driver.find_element_by_xpath("//input[@type='email']").send_keys("minhnguyen@novahub.vn")
    #     driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//input[@type='password']").send_keys("ducminh123")
    #     driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()
    @classmethod
    def tearDown(self):
        # self.driver.quit()
        print("done")