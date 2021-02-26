from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_CreateEmployee = "//main//button[@type='button']"
        self.col_Name = "//tr/th[contains(.,'Name')]"
        self.col_Email = "//tr/th[contains(.,'Email')]"
        self.col_Birthday = "//tr/th[contains(.,'Birthday')]"
        self.col_JoinDate = "//tr/th[contains(.,'Join date')]"
        self.col_PhoneNumber = "//tr/th[contains(.,'Phone number')]"
        self.col_Status = "//tr/th[contains(.,'Status')]"
        self.col_Actions = "//tr/th[contains(.,'Actions')]"
        self.txt_Search = "//input[@type='search']"
        self.drop_Status = "//select[@id='status-type']"
        self.opt_All = "//option[contains(.,'All')]"
        self.opt_Active = "//option[@value='ACTIVE']"
        self.opt_Former = "//option[@value='FORMER']"
        self.msg_noResult = "//div[@role='alert']"
        self.btn_Confirm = "//button[@class='btn btn-danger']"
        self.btn_Cancel = "//button[@class='btn btn-secondary']"
        self.btn_sort_name = "//table/thead/tr/th[contains (.,'Name')]"
        self.btn_sort_birthday = ""
        self.msg_Deactivate_success = "/html/body/div[@class='overlay-container']/div[@id='toast-container']/div[@class='ng-tns-c8-5 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success']"
        self.msg_Activate_success = "/html/body/div[@class='overlay-container']/div[@id='toast-container']/div[@class='ng-tns-c8-6 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success']"
        self.list_name = "//tbody/tr/td[1]"

    def enter_Search_term(self, search_term):
        self.driver.find_element_by_xpath(self.txt_Search).send_keys(search_term)

    def press_Search_button(self):
        self.driver.find_element_by_xpath(self.txt_Search).send_keys(Keys.ENTER)

    def delete_Search_term(self):
        self.driver.find_element_by_xpath(self.txt_Search).clear()

    def choose_Status(self, element):
        # self.driver.find_element_by_xpath(self.drop_Status).click()
        self.driver.find_element_by_xpath(element).click()

    def click_Edit_button(self, row):
        self.driver.find_element_by_xpath\
            ("//tbody/tr[" + str(row) + "]/td[7]//button[@class='btn btn-outline-primary mr-2']").click()

    def deactivate_Employee(self, row):
        self.driver.find_element_by_xpath\
            ("//tbody/tr[" + str(row) + "]/td[7]//button[@class='btn btn-outline-danger']").click()
        self.driver.find_element_by_xpath(self.btn_Confirm).click()

    def activate_Employee(self, row):
        self.driver.find_element_by_xpath\
            ("//tbody/tr[" + str(row) + "]/td[7]//button[@class='btn btn-outline-success']").click()
        self.driver.find_element_by_xpath(self.btn_Confirm).click()

    def click_create_button(self):
        self.driver.find_element(By.XPATH, self.btn_CreateEmployee).click()




