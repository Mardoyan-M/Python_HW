import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay(45)
    calculator_page.click_button_7()
    calculator_page.click_button_plus()
    calculator_page.click_button_8()
    calculator_page.click_button_equals()

    result = calculator_page.get_result()
    assert int(result) == 15
