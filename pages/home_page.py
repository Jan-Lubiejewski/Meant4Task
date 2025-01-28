from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # Locators
    _sign_in_button = (By.CLASS_NAME, "login")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_sign_in_button(self):
        # Call the click method from BasePage and pass the locator
        self.click(self._sign_in_button)
