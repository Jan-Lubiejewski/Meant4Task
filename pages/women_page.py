from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class WomenPage(BasePage):
    # Locators
    _blouse = (By.XPATH, "//a[@title='Blouse']")
    _sort_by = (By.ID, "selectProductSort")
    _product_prices = (By.XPATH, "//div[@class='product-container']//span[@itemprop='price']")
    _product_names = (By.XPATH, "//div[@class='product-container']//a[@class='product-name']")
    _white_product_option = (By.XPATH, "//div[@class='product-container']//a[@style='background:#ffffff;']")
    _left_price_handle = (By.XPATH, "//div[@id='layered_price_slider']//a[1]")
    _right_price_handle = (By.XPATH, "//div[@id='layered_price_slider']//a[2]")


    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_on_blouse(self):
        self.click(self._blouse)

    def select_sort_by_option_by_text(self, text):
        """
        Select sort by option.
        """
        self.select_by_visible_text(self._sort_by, text)

    def filter_by_color_link_text(self, text):
        """
        Filter by given color.
        Wait for the names to update.
        """
        # Get the old list of prices before moving the slider
        old_names = self.get_product_names()

        # Click the color
        color_locator = (By.PARTIAL_LINK_TEXT, text)
        self.click_without_wait(color_locator)

        # Wait until the names update
        WebDriverWait(self.driver, 10).until(
            lambda d: self.get_product_names() != old_names
        )
    
    def is_number_of_white_options_equal_number_of_products(self):
        """
        Return check if number of product with white color option is equal number of products.
        """
        white_options = self.find_elements_without_wait(self._white_product_option)
        product_names = self.get_product_names()

        return len(white_options) == len(product_names)

    def get_products_prices(self):
        """
        Return products prices in format: '$amount' as list.
        """
        prices = []
        elements = self.find_elements_without_wait(self._product_prices)
        for element in elements:
            prices.append(element.get_attribute("textContent").strip())
        return prices
    
    def is_prices_sorted_ascending(self, prices):
        """
        Convert prices to plain integers.
        Return check if the list is sorted asc.
        """
        # Convert price strings to integers (removing the '$' sign)
        numeric_prices = [int(price.replace("$", "")) for price in prices]
        # Check if the list is sorted in ascending order
        return numeric_prices == sorted(numeric_prices)
    
    def is_prices_sorted_descending(self, prices):
        """
        Convert prices to plain integers.
        Return check if the list is sorted desc.
        """
        # Convert price strings to integers (removing the '$' sign)
        numeric_prices = [int(price.replace("$", "")) for price in prices]
        # Check if the list is sorted in descending order
        return numeric_prices == sorted(numeric_prices, reverse=True)
    
    def get_product_names(self):
        """
        Return products names as list.
        """
        names = []
        elements = self.find_elements_without_wait(self._product_names)
        for element in elements:
            names.append(element.get_attribute("textContent").strip())
        return names
    
    def is_names_sorted_ascending(self, names):
        return names == sorted(names)
    
    def is_names_sorted_descending(self, names):
        return names == sorted(names, reverse=True)
    
    def move_price_slider_by_r_and_l_offset(self, left_offset, right_offset):
        """
        Slide the price slider by given handles offset.
        Wait for the prices to update.
        """
        # Get the old list of prices before moving the slider
        old_prices = self.get_products_prices()

        # Move the slider
        self.slide_slider(self._left_price_handle, self._right_price_handle,
                          left_offset, right_offset)
        
        # Wait until the prices update
        WebDriverWait(self.driver, 10).until(
            lambda d: self.get_products_prices() != old_prices
        )
    
    def is_prices_between(self, prices, min_price, max_price):
        """
        Convert prices to plain integers.
        Return check if the pricess are within min and max range.
        """
        # Convert price strings to integers (removing the '$' sign)
        numeric_prices = [int(price.replace("$", "").strip()) for price in prices]

        # Check if all prices are within range
        for numeric_price in numeric_prices:
            if numeric_price < min_price or numeric_price > max_price:
                return False
        return True
