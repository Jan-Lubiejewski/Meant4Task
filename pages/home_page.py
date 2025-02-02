from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    # Locators
    _sign_in_button = (By.CLASS_NAME, "login")
    _women_tab = (By.XPATH, "//ul[contains(@class, 'sf-menu')]//li")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_sign_in_button(self):
        # Call the click method from BasePage and pass the locator
        self.click(self._sign_in_button)

    def click_women_tab(self):
        '''
        Hover over women tab and click it.
        '''
        women_tab_element = self.find_element(self._women_tab)
        actions = ActionChains(self.driver)
        actions.move_to_element(women_tab_element).click().perform()
