import pytest
from selenium import webdriver
import time

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
    time.sleep(5)
    driver.quit()