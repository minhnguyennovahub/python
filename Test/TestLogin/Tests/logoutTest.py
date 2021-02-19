import time

from selenium import webdriver
import unittest

from Test.TestLogin.Pages.generalPage import GeneralPage
from Test.TestLogin.Pages.loginPage import LoginPage


class LogoutTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-helper-f21c1.web.app/login")
        self.driver.maximize_window()

    def test_Login_page_is_displayed_after_logging_out(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_Username_Password("admin@gmail.com", "123456")
        login.press_Login_button()
        driver.implicitly_wait(10)
        general = GeneralPage(driver)
        general.do_Logout()
        self.assertEqual(driver.find_element_by_xpath(login.txt_Email).is_displayed(), True)

    def test_Login_by_pasting_deeplink(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_Username_Password("admin@gmail.com", "123456")
        login.press_Login_button()
        time.sleep(5)
        deeplink = driver.current_url
        general = GeneralPage(driver)
        general.do_Logout()
        driver.get(deeplink)
        self.assertEqual(driver.find_element_by_xpath(login.txt_Email).is_displayed(), True)

    @classmethod
    def tearDown(self):
        self.driver.quit()