import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor="http://5.181.109.28:4444", options=options)
    yield driver
    if driver:
        driver.quit()