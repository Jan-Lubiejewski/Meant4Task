from pytest_bdd import scenarios, given, then
from pages.home_page import HomePage
from pages.women_page import WomenPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCarPage
from pages.authentication_page import AuthenticationPage

# Path to the feature files
scenarios('shopping_flow.feature')

@given('I am on "http://www.automationpractice.pl" Home Page')
def navigate_to_home_page(driver):
    driver.get("http://www.automationpractice.pl")

@then('I click on Women tab')
def click_on_women_tab(driver):
    home_page = HomePage(driver)
    home_page.click_women_tab()

@then('I click on Blouse')
def click_on_blouse(driver):
    women_page = WomenPage(driver)
    women_page.click_on_blouse()

@then('I choose "White" color and "M" size and click on "Add to cart"')
def choose_m_size_and_white_color_then_order(driver):
    product_page = ProductPage(driver)
    product_page.select_color(0)  # White is first color in the list
    # product_page.select_size("M")
    product_page.click_add_to_cart()

@then('I click "Proceed to checkout" and I get redirected to Shopping Cart Page')
def click_on_proceed_to_checkout_in_product_page(driver):
    product_page = ProductPage(driver)
    product_page.click_proceed_to_checkout()

@then('In shopping cart I click "Proceed to checkout"')
def click_on_proceed_to_checkout_in_shopping_cart(driver):
    shopping_cart_page = ShoppingCarPage(driver)
    shopping_cart_page.click_summary_proceed_to_checkout()

@then("I login using valid credentials")
def login_using_valid_credentials(driver):
    authentication_page = AuthenticationPage(driver)
    authentication_page.fill_sign_in_email("jkli2@gmail.com")
    authentication_page.fill_password("123456")
    authentication_page.click_sign_in_button()

@then('On address tab I click "Proceed to checkout"')
def click_on_proceed_to_checkout_in_shopping_cart(driver):
    shopping_cart_page = ShoppingCarPage(driver)
    shopping_cart_page.click_address_proceed_to_checkout()

@then('On shipping tab I agree to terms of service and click "Proceed to checkout"')
def click_on_proceed_to_checkout_in_shopping_cart(driver):
    shopping_cart_page = ShoppingCarPage(driver)
    shopping_cart_page.click_terms_of_service_checkbox()
    shopping_cart_page.click_shipping_proceed_to_checkout()

@then('I choose to pay by bank wire')
def click_on_pay_by_bank_wire(driver):
    shopping_cart_page = ShoppingCarPage(driver)
    shopping_cart_page.click_pay_by_bank_wire()

@then('I click "I confirm my order"')
def click_on_pay_by_bank_wire(driver):
    shopping_cart_page = ShoppingCarPage(driver)
    shopping_cart_page.click_confirm_order_button()

@then('The green alert "Your order on My Shop is complete." should appear')
def check_purchase_success_alert_message(driver):
    shopping_cart_page = ShoppingCarPage(driver)
    expected_alert_message = "Your order on My Shop is complete."
    actual_alert_message = shopping_cart_page.get_purchase_success_alert_text()

    assert actual_alert_message == expected_alert_message, \
    f"Expected error message to be '{expected_alert_message}' " \
    f"but got '{actual_alert_message}'"