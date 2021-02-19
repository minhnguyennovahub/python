class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.txt_email = "//input[@type='email']"
        self.btn_next = "//button[@type='submit']"
        self.btn_return = "//button[@type='button']"
        self.txt_token = "//input[@type='number']"
        self.txt_newPassword = "//input[@formcontrolname='newPassword']"
        self.txt_confirmPassword = "//input[@formcontrolname='confirmPassword']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.txt_email).send_keys(username)

    def click_next_button(self):
        self.driver.find_element_by_xpath(self.btn_next).click()