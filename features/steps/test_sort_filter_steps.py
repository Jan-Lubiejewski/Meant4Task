from pytest_bdd import scenarios, given, then, parsers
from pages.home_page import HomePage
from pages.women_page import WomenPage

# Path to the feature files
scenarios('sorting_and_filtering.feature')

@given('I am on "http://www.automationpractice.pl" Home Page')
def navigate_to_home_page(driver):
    driver.get("http://www.automationpractice.pl")

@then('I click on Women tab')
def click_on_women_tab(driver):
    home_page = HomePage(driver)
    home_page.click_women_tab()

@given(parsers.parse('I choose Sort by "{sort_option}"'))
def sort_by(driver, sort_option):
    women_page = WomenPage(driver)
    women_page.select_sort_by_option_by_text(sort_option)

@then('The prices should be sorted in ascending order')
def is_prices_sorted_asc(driver):
    women_page = WomenPage(driver)
    prices = women_page.get_products_prices()
    is_sorted_asc = women_page.is_prices_sorted_ascending(prices)
    assert is_sorted_asc == True

@then('The prices should be sorted in descending order')
def is_prices_sorted_desc(driver):
    women_page = WomenPage(driver)
    prices = women_page.get_products_prices()
    is_sorted_desc = women_page.is_prices_sorted_descending(prices)
    assert is_sorted_desc == True

@then('The names should be sorted in ascending order')
def is_names_sorted_asc(driver):
    women_page = WomenPage(driver)
    names = women_page.get_product_names()
    is_sorted_asc = women_page.is_names_sorted_ascending(names)
    assert is_sorted_asc == True

@then('The names should be sorted in descending order')
def is_names_sorted_desc(driver):
    women_page = WomenPage(driver)
    names = women_page.get_product_names()
    is_sorted_desc = women_page.is_names_sorted_descending(names)
    assert is_sorted_desc == True

@given(parsers.parse('I choose Filter by "{color}" color'))
def filter_by_color(driver, color):
    women_page = WomenPage(driver)
    women_page.filter_by_color_link_text(color)

@then('Products only with given "White" color option should appear')
def is_products_with_color_appear(driver):
    women_page = WomenPage(driver)
    assert women_page.is_number_of_white_options_equal_number_of_products() == True

@given('I choose price range to be "between 16$ and 28$"')
def filter_by_price_between_16_and_28(driver):
    women_page = WomenPage(driver)
    women_page.move_price_slider_by_r_and_l_offset(0, -165)

@then('The prices should be higher than 16$ and lower than 28$')
def is_prices_between_16_and_28(driver):
    women_page = WomenPage(driver)
    prices = women_page.get_products_prices()
    is_between_16_and_18 = women_page.is_prices_between(prices, 16, 28)
    assert is_between_16_and_18 == True