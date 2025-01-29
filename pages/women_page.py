from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WomenPage(BasePage):
    # Locators
    _blouse = (By.XPATH, "//a[@title='Blouse']")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_on_blouse(self):
        self.click(self._blouse)