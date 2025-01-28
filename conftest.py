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

    # This is the "Setup" part: Visit the given page before each scenario.
    yield driver
    
    # This is the "Teardown" part: Quit the driver after each scenario.
    time.sleep(4) # Wait for debug purposes
    driver.quit()