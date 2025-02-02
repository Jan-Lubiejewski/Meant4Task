from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ShoppingCarPage(BasePage):
    # Locators
    _summary_proceed_to_checkout_button = (By.XPATH,"//p//a[@title='Proceed to checkout']")
    _address_proceed_to_checkout_button = (By.XPATH,"//button[@name='processAddress']")
    _shipping_proceed_to_checkout_button = (By.XPATH,"//button[@name='processCarrier']")
    _terms_of_service_checkbox = (By.ID,"cgv")
    _pay_by_bank_wire = (By.XPATH,"//a[@title='Pay by bank wire']")
    _confirm_order_button = (By.XPATH, "//button[span[contains(text(), 'I confirm my order')]]")
    _alert_success = (By.XPATH, "//p[@class='alert alert-success']")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_summary_proceed_to_checkout(self):
        self.click(self._summary_proceed_to_checkout_button)

    def click_address_proceed_to_checkout(self):
        self.click(self._address_proceed_to_checkout_button)

    def click_shipping_proceed_to_checkout(self):
        self.click(self._shipping_proceed_to_checkout_button)

    def click_terms_of_service_checkbox(self):
        self.check(self._terms_of_service_checkbox)

    def click_pay_by_bank_wire(self):
        self.click(self._pay_by_bank_wire)

    def click_confirm_order_button(self):
        self.click(self._confirm_order_button)

    def get_purchase_success_alert_text(self):
        """
        Return the text of the green success alert if it is visible.
        """
        element = self.find_element(self._alert_success)
        return element.text
