from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WomenPage(BasePage):
    # Locators
    _blouse = (By.XPATH, "//a[@title='Blouse']")
    _sort_by = (By.ID, "selectProductSort")
    _product_prices = (By.XPATH, "//div[@class='product-container']//span[@itemprop='price']")
    _product_names = (By.XPATH, "//div[@class='product-container']//a[@class='product-name']")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_on_blouse(self):
        self.click(self._blouse)

    def select_sort_by_option_by_text(self, text):
        self.select_by_visible_text(self._sort_by, text)

    def get_product_prices(self):
        prices = []
        elements = self.find_elements_without_wait(self._product_prices)
        for element in elements:
            prices.append(element.get_attribute("textContent").strip())
        return prices
    
    def is_prices_sorted_ascending(self, prices):
        # Convert price strings to integers (removing the '$' sign)
        numeric_prices = [int(price.replace("$", "")) for price in prices]
        # Check if the list is sorted in ascending order
        return numeric_prices == sorted(numeric_prices)
    
    def is_prices_sorted_descending(self, prices):
        # Convert price strings to integers (removing the '$' sign)
        numeric_prices = [int(price.replace("$", "")) for price in prices]
        # Check if the list is sorted in descending order
        return numeric_prices == sorted(numeric_prices, reverse=True)
    
    def get_product_names(self):
        names = []
        elements = self.find_elements_without_wait(self._product_names)
        for element in elements:
            names.append(element.get_attribute("textContent").strip())
        return names
    
    def is_names_sorted_ascending(self, names):
        return names == sorted(names)
    
    def is_names_sorted_descending(self, names):
        return names == sorted(names, reverse=True)