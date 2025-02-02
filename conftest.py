import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    """
    Setup: Create a WebDriver instance before each scenario.
    Teardown: Quit the WebDriver instance after each scenario.
    """
    # Set up the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    
    # Teardown
    driver.quit()