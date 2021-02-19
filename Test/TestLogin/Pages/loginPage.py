class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.txt_Email = "//input[@type='email']"
        self.txt_Password = "//input[@type='password']"
        self.btn_Login = "//button[@type='submit']"
        self.error_msg = "//form//div[contains(.,'Email')]"
        self.error_msg2 = "//div[@id='toast-container']"
        self.btn_forgot = "//a[@type='button']"

    def enter_Username_Password (self, username, password):
        self.driver.find_element_by_xpath(self.txt_Email).send_keys(username)
        self.driver.find_element_by_xpath(self.txt_Password).send_keys(password)

    def press_Login_button(self):
        self.driver.find_element_by_xpath(self.btn_Login).click()

    def click_Forgot_Password(self):
        self.driver.find_element_by_xpath(self.btn_forgot).click()