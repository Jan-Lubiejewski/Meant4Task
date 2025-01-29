from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AuthenticationPage(BasePage):
    # Locators
    _email_create_account_field = (By.ID, "email_create")
    _email_create_account_error_alert = (By.XPATH, "//div[@id='create_account_error']//li")
    _email_sign_in_field = (By.ID, "email")
    _password = (By.ID, "passwd")
    _create_account_button = (By.XPATH, "//button[@id='SubmitCreate']")
    _sign_in_button = (By.ID, "SubmitLogin")
    _sign_in_error_alert = (By.XPATH, "//div[@class='alert alert-danger']//li")

    def __init__(self, driver):
        super().__init__(driver)

    def click_create_account_button(self):
        self.click(self._create_account_button)

    def click_sign_in_button(self):
        self.click(self._sign_in_button)

    def get_email_create_account_error_alert_text(self):
        element = self.find_element(self._email_create_account_error_alert)
        return element.text
    
    def get_sign_in_alert_text(self):
        element = self.find_element(self._sign_in_error_alert)
        return element.text
    
    def fill_create_account_email(self, email):
        self.send_keys(self._email_create_account_field, email)

    def fill_sign_in_email(self, email):
        self.send_keys(self._email_sign_in_field, email)

    def fill_password(self, password):
        self.send_keys(self._password, password)
    

    