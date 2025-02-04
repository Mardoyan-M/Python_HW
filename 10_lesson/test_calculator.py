import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Проверка сложения двух чисел в калькуляторе")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()

    with allure.step("Установить задержку"):
        calculator_page.set_delay(45)

    with allure.step("Нажать кнопку 7"):
        calculator_page.click_button_7()

    with allure.step("Нажать кнопку +"):
        calculator_page.click_button_plus()

    with allure.step("Нажать кнопку 8"):
        calculator_page.click_button_8()

    with allure.step("Нажать кнопку ="):
        calculator_page.click_button_equals()

    with allure.step("Получить результат"):
        result = calculator_page.get_result()

    with allure.step("Проверить, что результат равен 15"):
        assert int(result) == 15
