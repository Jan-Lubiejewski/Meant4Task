from pytest_bdd import scenarios, given, when, then
from faker import Faker
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.create_account_page import CreateAccountPage
from pages.my_account_page import MyAccountPage

# Path to the feature files
scenarios('registration.feature')

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
def check_email_create_account_error_message(driver):
    authentication_page = AuthenticationPage(driver)
    expected_error_message = "Invalid email address."
    actual_error_message = authentication_page.get_email_create_account_error_alert_text()

    assert actual_error_message == expected_error_message, \
    f"Expected error message to be '{expected_error_message}' " \
    f"but got '{actual_error_message}'"

@given('I fill Email address with "qamyk1258@gmail.com" and click on Create an account button')
def fill_email(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_create_account_email("qamyk1258@gmail.com")
    authentication_page.click_create_account_button()

@then("I clear all fields and click on Register button")
def clear_all_fields_and_click_register(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.clear_all_fields()
    create_account_page.click_register_button()

@then("The red alerts for all required fields should appear")
def check_req_field_error_messages(driver):
    create_account_page = CreateAccountPage(driver)
    messages = create_account_page.get_all_error_messages()

    assert "lastname is required" in messages[0].text, \
        f"Expected 'lastname is required' in the first error message" \
        f"but got '{messages[0].text}'"
    
    assert "firstname is required" in messages[1].text, \
        f"Expected 'firstname is required' in the second error message" \
        f"but got '{messages[1].text}'"
    
    assert "email is required" in messages[2].text, \
        f"Expected 'email is required' in the third error message" \
        f"but got '{messages[2].text}'"
    
    assert "passwd is required" in messages[3].text, \
        f"Expected 'passwd is required' in the forth error message" \
        f"but got '{messages[3].text}'"
    
@then('I fill first name with "123" and rest of required fields with valid data and click on Register button')
def fill_invalid_first_name(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.fill_first_name("123")
    create_account_page.fill_last_name("Kowalski")
    create_account_page.fill_email("qamyk1258@gmail.com")
    create_account_page.fill_password("12345")
    create_account_page.click_register_button()

@then('The red alert "firstname is invalid" should appear')
def check_invalid_first_name_error_message(driver):
    create_account_page = CreateAccountPage(driver)
    messages = create_account_page.get_all_error_messages()

    assert "firstname is invalid" in messages[0].text, \
        f"Expected error message to be 'firstname is invalid'" \
        f"but got '{messages[0].text}'"
    
@then('I fill last name with "123" and rest of required fields with valid data and click on Register button')
def fill_invalid_first_name(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.fill_first_name("Jan")
    create_account_page.fill_last_name("123")
    create_account_page.fill_email("qamyk1258@gmail.com")
    create_account_page.fill_password("12345")
    create_account_page.click_register_button()

@then('The red alert "lastname is invalid" should appear')
def check_invalid_first_name_error_message(driver):
    create_account_page = CreateAccountPage(driver)
    messages = create_account_page.get_all_error_messages()

    assert "lastname is invalid" in messages[0].text, \
        f"Expected error message to be 'lastname is invalid'" \
        f"but got '{messages[0].text}'"
    
@then('I fill email again with "123" and rest of required fields with valid data and click on Register button')
def fill_invalid_first_name(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.fill_first_name("Jan")
    create_account_page.fill_last_name("Kowalski")
    create_account_page.fill_email("123")
    create_account_page.fill_password("12345")
    create_account_page.click_register_button()

@then('The red alert "email is invalid" should appear')
def check_invalid_first_name_error_message(driver):
    create_account_page = CreateAccountPage(driver)
    messages = create_account_page.get_all_error_messages()

    assert "email is invalid" in messages[0].text, \
        f"Expected error message to be 'email is invalid'" \
        f"but got '{messages[0].text}'"
    
@then('I fill password with "123" and rest of required fields with valid data and click on Register button')
def fill_invalid_first_name(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.fill_first_name("Jan")
    create_account_page.fill_last_name("Kowalski")
    create_account_page.fill_email("qamyk1258@gmail.com")
    create_account_page.fill_password("123")
    create_account_page.click_register_button()

@then('The red alert "passwd is invalid" should appear')
def check_invalid_first_name_error_message(driver):
    create_account_page = CreateAccountPage(driver)
    messages = create_account_page.get_all_error_messages()

    assert "passwd is invalid" in messages[0].text, \
        f"Expected error message to be 'passwd is invalid'" \
        f"but got '{messages[0].text}'"
    
@then('I fill all the required fields with valid data and click on Register button')
def fill_invalid_first_name(driver):
    fake = Faker()
    random_mail = fake.email()
    create_account_page = CreateAccountPage(driver)
    create_account_page.fill_first_name("Jan")
    create_account_page.fill_last_name("Kowalski")
    create_account_page.fill_email(random_mail)
    create_account_page.fill_password("12345")
    create_account_page.click_register_button()

@then('I get redirected to My Account Page and green alert "Your account has been created" appears')
def redirect_to_authentication_page(driver):
    authentication_page = MyAccountPage(driver)
    expected_title = "My account - My Shop"
    actual_title = authentication_page.get_page_title()

    assert actual_title == expected_title, \
        f"Expected page title to be '{expected_title}' " \
        f"but got '{actual_title}'"
    
    expected_alert_message = "Your account has been created."
    actual_alert_message = authentication_page.get_green_alert_text()

    assert actual_alert_message == expected_alert_message, \
    f"Expected error message to be '{expected_alert_message}' " \
    f"but got '{actual_alert_message}'"
    
