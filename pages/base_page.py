from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    def get_page_title(self):
        """
        Return the title of the current page.
        """
        return self.driver.title
