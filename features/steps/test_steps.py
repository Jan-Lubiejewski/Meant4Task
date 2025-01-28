from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage

# Path to the feature files
scenarios('example.feature')

@given('I am on "http://www.automationpractice.pl" Home Page')
def navigate_to_home_page(driver):
    driver.get("http://www.automationpractice.pl")

@when('I click on "Sign in" button')
def click_on_sign_in_button(driver):
    home_page = HomePage(driver)
    home_page.click_sign_in_button()

@then('I get redirected to Authentication Page')
def redirect_to_authentication_page(driver):
    authentication_page = AuthenticationPage(driver)
    expected_title = "Login - My Shop"
    actual_title = authentication_page.get_page_title()
    assert actual_title == expected_title, \
        f"Expected page title to be '{expected_title}' " \
        f"but got '{actual_title}'"
    
@given('I do not fill Email address and click on "Create an account" button')
def create_account_with_empty_email(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.click_create_account_button()

@then('The red alert "Invalid email address" should appear')
def check_email_error_message(driver):
    authentication_page = AuthenticationPage(driver)
    expected_error_message = "Invalid email address."
    actual_error_message = authentication_page.get_email_error_alert_text()
    assert actual_error_message == expected_error_message, \
    f"Expected error message to be '{expected_error_message}' " \
    f"but got '{actual_error_message}'"

@given('I fill Email address with "qamyk1258@gmail.com" and click on Create an account button')
def fill_email(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_email("qamyk1258@gmail.com")
    authentication_page.click_create_account_button()