import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MinhCommons:
    def __init__(self, driver):
        self.driver = driver

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def wait_displayed(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))

    def random_string(self, length):
        self.letters = string.ascii_lowercase
        self.result_str = ''.join(random.choice(self.letters) for i in range(length))
        return self.result_str

