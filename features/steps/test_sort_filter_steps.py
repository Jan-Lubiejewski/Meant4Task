from pytest_bdd import scenarios, given, then
from pages.home_page import HomePage
from pages.women_page import WomenPage
import time
# Path to the feature files
scenarios('sorting_and_filtering.feature')

@given('I am on "http://www.automationpractice.pl" Home Page')
def navigate_to_home_page(driver):
    driver.get("http://www.automationpractice.pl")

@then('I click on Women tab')
def click_on_women_tab(driver):
    home_page = HomePage(driver)
    home_page.click_women_tab()

@given('I choose Sort by "Price: Lowest first"')
def sort_by_price_lowest_first(driver):
    women_page = WomenPage(driver)
    women_page.select_sort_by_option_by_text("Price: Lowest first")

@then('The prices should be sorted in ascending order')
def is_prices_sorted_asc(driver):
    women_page = WomenPage(driver)
    prices = women_page.get_product_prices()
    is_sorted_asc = women_page.is_prices_sorted_ascending(prices)
    assert is_sorted_asc == True

@given('I choose Sort by "Price: Highest first"')
def sort_by_price_highest_first(driver):
    women_page = WomenPage(driver)
    women_page.select_sort_by_option_by_text("Price: Highest first")

@then('The prices should be sorted in descending order')
def is_prices_sorted_desc(driver):
    women_page = WomenPage(driver)
    prices = women_page.get_product_prices()
    is_sorted_desc = women_page.is_prices_sorted_descending(prices)
    assert is_sorted_desc == True

@given('I choose Sort by "Product Name: A to Z"')
def sort_by_names_a_to_z(driver):
    women_page = WomenPage(driver)
    women_page.select_sort_by_option_by_text("Product Name: A to Z")

@then('The names should be sorted in ascending order')
def is_names_sorted_asc(driver):
    women_page = WomenPage(driver)
    names = women_page.get_product_names()
    is_sorted_asc = women_page.is_names_sorted_ascending(names)
    assert is_sorted_asc == True

@given('I choose Sort by "Product Name: Z to A"')
def sort_by_names_z_to_a(driver):
    women_page = WomenPage(driver)
    women_page.select_sort_by_option_by_text("Product Name: Z to A")

@then('The names should be sorted in descending order')
def is_names_sorted_desc(driver):
    women_page = WomenPage(driver)
    names = women_page.get_product_names()
    is_sorted_desc = women_page.is_names_sorted_descending(names)
    assert is_sorted_desc == True

@given('I choose price range to be "between 16$ and 28$"')
def filter_by_price_between_16_and_28(driver):
    women_page = WomenPage(driver)
    women_page.move_price_slider_by_r_and_l_offset(0, -165)

@then('The prices should be higher than 16$ and lower than 28$')
def is_prices_between_16_and_28(driver):
    women_page = WomenPage(driver)
    prices = women_page.get_product_prices()
    is_between_16_and_18 = women_page.is_prices_between(prices, 16, 28)
    assert is_between_16_and_18 == True