class EditEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.editPage_url = "https://admin-helper-f21c1.web.app/employees/1/edit"
        self.txt_Firstname = "//input[@id='firstName']"
        self.txt_Lastname = "//input[@id='lastName']"
        self.txt_Email = "//input[@id='email']"
        self.txt_Birthday = "//input[@id='birthdate']"
        self.txt_Phone = "//input[@id='phone']"
        self.txt_Joindate = "//input[@id='joinDate']"
        self.btn_Save = "//button[@type='submit']"
        self.btn_Detail = "//button[@type='button']"
        self.msg_edit_success = "//div[@class='ng-tns-c8-0 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success']"
    def edit_profile(self, first_name, last_name, email, birth_day, phone_number, join_date):
        # Input First name
        self.driver.find_element_by_xpath(self.txt_Firstname).clear()
        self.driver.find_element_by_xpath(self.txt_Firstname).send_keys(first_name)

        # Input Last name
        self.driver.find_element_by_xpath(self.txt_Lastname).clear()
        self.driver.find_element_by_xpath(self.txt_Lastname).send_keys(last_name)

        # Input Email
        self.driver.find_element_by_xpath(self.txt_Email).clear()
        self.driver.find_element_by_xpath(self.txt_Email).send_keys(email)

        # Input Birthday
        self.driver.find_element_by_xpath(self.txt_Birthday).clear()
        self.driver.find_element_by_xpath(self.txt_Birthday).send_keys(birth_day)

        # Input Phone number
        self.driver.find_element_by_xpath(self.txt_Phone).clear()
        self.driver.find_element_by_xpath(self.txt_Phone).send_keys(phone_number)

        # Input Join Date
        self.driver.find_element_by_xpath(self.txt_Joindate).clear()
        self.driver.find_element_by_xpath(self.txt_Joindate).send_keys(join_date)

    def click_save_button(self):
        self.driver.find_element_by_xpath(self.btn_Save).click()

