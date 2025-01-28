from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MyAccountPage(BasePage):
    # Locators
    _green_alert = (By.CLASS_NAME, "alert-success")
    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def get_green_alert_text(self):
        """
        This method will return the text of the green success alert if it is visible.
        """
        element = self.find_element(self._green_alert)
        return element.text
