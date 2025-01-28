from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AuthenticationPage(BasePage):
    #Locators
    _create_account_button = (By.XPATH, "//button[@id='SubmitCreate']")
    _email_field = (By.ID, "email_create")
    _email_error_alert = (By.XPATH, "//div[@id='create_account_error']//li")

    def __init__(self, driver):
        super().__init__(driver)

    def click_create_account_button(self):
        self.click(self._create_account_button)

    def get_email_error_alert_text(self):
        """
        This method will return the text of the email error alert if it is visible.
        """
        element = self.find_element(self._email_error_alert)
        return element.text
    
    def fill_email(self, email):
        self.send_keys(self._email_field, email)
    

    