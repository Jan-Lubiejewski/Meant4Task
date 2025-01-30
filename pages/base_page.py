from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator):
        """
        Returns the web element found by locator
        """
        return self.wait_for_element(*locator)
    
    def find_elements(self, locator):
        """
        Returns a list of web elements found by locator
        """
        return self.wait_for_elements(*locator)
    
    def find_elements_without_wait(self, locator):
        return self.driver.find_elements(*locator)
    
    def slide_slider(self, left_handle_loc, right_handle_loc, left_offset, right_offset):
        left_handle = self.driver.find_element(*left_handle_loc)
        right_handle = self.driver.find_element(*right_handle_loc)
        actions = ActionChains(self.driver)
        actions.click_and_hold(left_handle).move_by_offset(left_offset, 0).release().perform()
        actions.click_and_hold(right_handle).move_by_offset(right_offset, 0).release().perform()

    
    def send_keys(self, locator, value):
        element = self.wait_for_element(*locator)
        element.clear()
        element.send_keys(value)

    def clear(self, locator):
        element = self.wait_for_element(*locator)
        element.clear()
    
    def click(self, locator):
        """
        Clicks on an element using the locator passed from the page class
        """
        element = self.wait_for_element(*locator)
        element.click()

    def check(self, locator):
        """
        Ensures the checkbox is checked.
        If it is already checked, it does nothing.
        """
        element = self.driver.find_element(*locator)
        if not element.is_selected():
            element.click()

    def select_by_visible_text(self, locator, text):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def wait_for_element(self, by, value, timeout=10):
        """
        Wait for an element to become visible
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    
    def wait_for_elements(self, by, value, timeout=10):
        """
        Wait for multiple elements to become visible
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )
    
    def wait_for_element_displayed_none(self, by, value, timeout=10):
        """
        Wait for an element to have the style 'display: none'
        """
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(by, value).value_of_css_property("display") == "none"
        )
    
    def get_page_title(self):
        """
        Return the title of the current page.
        """
        return self.driver.title
