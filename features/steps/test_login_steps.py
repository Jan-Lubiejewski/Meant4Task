from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.my_account_page import MyAccountPage

# Path to the feature files
scenarios('login.feature')

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
    
@given('I do not fill email and password and click on "Sign in" button')
def sign_in_with_empty_email_and_password(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.click_sign_in_button()

@then('The red alert "An email address required." should appear')
def check_email_sign_in_error_message(driver):
    authentication_page = AuthenticationPage(driver)
    expected_error_message = "An email address required."
    actual_error_message = authentication_page.get_sign_in_alert_text()

    assert actual_error_message == expected_error_message, \
    f"Expected error message to be '{expected_error_message}' " \
    f"but got '{actual_error_message}'"

@given('I fill email with "jkli2@gmail.com" and do not fill password and click on "Sign in" button')
def fill_valid_email_and_empty_password(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_sign_in_email("jkli2@gmail.com")
    authentication_page.click_sign_in_button()

@then('The red alert "Password is required." should appear')
def check_email_sign_in_error_message(driver):
    authentication_page = AuthenticationPage(driver)
    expected_error_message = "Password is required."
    actual_error_message = authentication_page.get_sign_in_alert_text()

    assert actual_error_message == expected_error_message, \
    f"Expected error message to be '{expected_error_message}' " \
    f"but got '{actual_error_message}'"


@given('I do not fill email and fill password with "123456" and click on "Sign in" button')
def fill_valid_email_and_empty_password(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_password("123456")
    authentication_page.click_sign_in_button()

@given('I fill email with "jkli2@gmail.com" and fill password with "12345" and click on "Sign in" button')
def fill_valid_email_and_empty_password(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_sign_in_email("jkli2@gmail.com")
    authentication_page.fill_password("12345")
    authentication_page.click_sign_in_button()

@then('The red alert "Authentication failed." should appear')
def check_email_sign_in_error_message(driver):
    authentication_page = AuthenticationPage(driver)
    expected_error_message = "Authentication failed."
    actual_error_message = authentication_page.get_sign_in_alert_text()

    assert actual_error_message == expected_error_message, \
    f"Expected error message to be '{expected_error_message}' " \
    f"but got '{actual_error_message}'"

@given('I fill email with "jkli2@gmail.com" and fill password with "123456" and click on "Sign in" button')
def fill_valid_email_and_empty_password(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_sign_in_email("jkli2@gmail.com")
    authentication_page.fill_password("123456")
    authentication_page.click_sign_in_button()

@then('I get redirected to My Account Page')
def redirect_to_authentication_page(driver):
    authentication_page = MyAccountPage(driver)
    expected_title = "My account - My Shop"
    actual_title = authentication_page.get_page_title()

    assert actual_title == expected_title, \
        f"Expected page title to be '{expected_title}' " \
        f"but got '{actual_title}'"
