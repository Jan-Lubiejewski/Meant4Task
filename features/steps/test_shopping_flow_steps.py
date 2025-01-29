from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage

# Path to the feature files
scenarios('shopping_flow.feature')

@given('I am on "http://www.automationpractice.pl" Home Page')
def navigate_to_home_page(driver):
    driver.get("http://www.automationpractice.pl")

@when('I click on Women tab')
def click_on_women_tab(driver):
    home_page = HomePage(driver)
    home_page.click_women_tab()