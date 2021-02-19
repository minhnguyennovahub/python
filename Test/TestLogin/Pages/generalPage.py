class GeneralPage:
    def __init__(self, driver):
        self.driver = driver
        self.drop_profile = "//div/img[@alt='user@email.com']"
        self.btn_Info = "//a[contains(.,'Information')]"
        self.btn_ChangePW = "//a[contains(.,'Change password')]"
        self.btn_Logout = "//a[contains(.,'Logout')]"
    def do_Logout(self):
        self.driver.find_element_by_xpath(self.drop_profile).click()
        self.driver.find_element_by_xpath(self.btn_Logout).click()