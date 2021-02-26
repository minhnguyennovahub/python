from selenium.webdriver.common.by import By


class CreateEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://admin-helper-f21c1.web.app/employees/create"
        self.txt_Firstname = "//input[@id='firstName']"
        self.txt_Lastname = "//input[@id='lastName']"
        self.txt_Email = "//input[@id='email']"
        self.txt_Pass = "//input[@id='pass']"
        self.txt_Confirm_Pass = "//input[@id='confirmPassword']"
        self.txt_Birthday = "//input[@id='birthdate']"
        self.txt_Phone = "//input[@id='phone']"
        self.txt_Joindate = "//input[@id='joinDate']"
        self.btn_Save = "//button[@type='submit']"
        self.btn_Detail = "//button[@type='button']"
        self.msg_create_success = "//div[@class='ng-tns-c8-0 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success']"
        self.msg_firstname_required = "//div[@class='invalid-feedback']/div[contains(.,' First ')]"
        self.msg_lastname_required = "//div[@class='invalid-feedback']/div[contains(.,' Last')]"
        self.msg_error_email = "//div[@class='invalid-feedback']/div[contains(.,' Email')]"
        self.msg_email_required = "//div[@id='toast-container' and contains(.,' Email')]"
        self.msg_error_birthday = "//form/div/div/div[contains(.,'Birthday c')]"
        self.msg_error_phone = "//form/div/div/div[contains(.,'Phone number ')]"

    def create_profile(self, first_name, last_name, email,  password, confirm_password, birth_day, phone_number, join_date):
        # Input First name
        self.driver.find_element_by_xpath(self.txt_Firstname).send_keys(first_name)

        # Input Last name
        self.driver.find_element_by_xpath(self.txt_Lastname).send_keys(last_name)

        # Input Email
        self.driver.find_element_by_xpath(self.txt_Email).send_keys(email)

        # Input password
        self.driver.find_element_by_xpath(self.txt_Pass).send_keys(password)

        # Input confirm password
        self.driver.find_element_by_xpath(self.txt_Confirm_Pass).send_keys(confirm_password)

        # Input Birthday
        self.driver.find_element_by_xpath(self.txt_Birthday).send_keys(birth_day)

        # Input Phone number
        self.driver.find_element_by_xpath(self.txt_Phone).send_keys(phone_number)

        # Input Join Date
        self.driver.find_element_by_xpath(self.txt_Joindate).send_keys(join_date)

    def click_save_button(self):
        self.driver.find_element_by_xpath(self.btn_Save).click()

    def get_email(self, row):
        return self.driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[@class='align-middle'][2]").text

