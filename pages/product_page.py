from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ProductPage(BasePage):
    # Locators
    _size_picker = (By.ID, "group_1")
    _color_picker = (By.XPATH, "//ul[@id='color_to_pick_list']//li")
    _add_to_cart = (By.ID, "add_to_cart")
    _proceed_to_checkout_button = (By.XPATH, "//a[@title='Proceed to checkout']")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_on_blouse(self):
        self.click(self._blouse)
    
    def select_size(self, text):
        self.select_by_visible_text(self._size_picker, text)

    def select_color(self, value):
        """
        Wait for "Add to cart" button to vanish.
        Select the product color.
        """
        # Wait for "Add to cart" button to be in 'display: none'
        # Changing color without it result in Add to cart not being displayed
        self.wait_for_element_displayed_none(*self._add_to_cart)
        
        # Select color
        color_elements = self.find_elements(self._color_picker)  # List of WebElements
        color_elements[value].click()

    def click_add_to_cart(self):
        self.click(self._add_to_cart)

    def click_proceed_to_checkout(self):
        self.click(self._proceed_to_checkout_button)
