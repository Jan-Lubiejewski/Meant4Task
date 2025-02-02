from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CreateAccountPage(BasePage):
    # Locators
    _mr_radio = (By.ID, "id_gender1")
    _mrs_radio = (By.ID, "id_gender2")
    _first_name = (By.ID, "customer_firstname")
    _last_name = (By.ID, "customer_lastname")
    _email = (By.ID, "email")
    _password = (By.ID, "passwd")
    _day = (By.ID, "days")
    _month = (By.ID, "months")
    _year = (By.ID, "years")
    _newsletter_check = (By.ID, "newsletter")
    _register_button = (By.ID, "submitAccount")
    _alert_messages = (By.XPATH, "//div[@class='alert alert-danger']//li")

    def __init__(self, driver):
        # Initialize the base class with the driver
        super().__init__(driver)

    def click_mr_radio(self):
        self.click(self._mr_radio)

    def click_mrs_radio(self):
        self.click(self._mrs_radio)

    def fill_first_name(self, first_name):
        self.send_keys(self._first_name, first_name)

    def fill_last_name(self, last_name):
        self.send_keys(self._last_name, last_name)

    def fill_email(self, email):
        self.send_keys(self._email, email)
    
    def fill_password(self, password):
        self.send_keys(self._password, password)

    def select_day(self, day):
        self.wait_for_element(*self._day)
        self.select_by_value(self._day, day)

    def select_month(self, month):
        self.wait_for_element(*self._month)
        self.select_by_value(self._month, month)

    def select_year(self, year):
        self.wait_for_element(*self._year)
        self.select_by_value(self._year, year)

    def check_newsletter(self):
        self.check(self._newsletter_check)

    def click_register_button(self):
        self.click(self._register_button)

    def clear_all_fields(self):
        self.clear(self._first_name)
        self.clear(self._last_name)
        self.clear(self._email)
        self.clear(self._password)

    def get_all_error_messages(self):
        return self.find_elements(self._alert_messages)

    
    

    