import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тест покупки товаров")
@allure.description("Проверка процесса покупки товаров на сайте")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.NORMAL)
def test_shop(driver):
    with allure.step("Открыть сайт"):
        driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    with allure.step("Ввести имя пользователя"):
        login_page.enter_username("standard_user")

    with allure.step("Ввести пароль"):
        login_page.enter_password("secret_sauce")

    with allure.step("Нажать кнопку входа"):
        login_page.click_login_button()

    product_page = ProductPage(driver)

    with allure.step("Добавить товары в корзину"):
        product_page.add_to_cart('add-to-cart-sauce-labs-backpack')
        product_page.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
        product_page.add_to_cart('add-to-cart-sauce-labs-onesie')

    with allure.step("Перейти в корзину"):
        product_page.go_to_cart()

    with allure.step("Начать процесс оформления заказа"):
        product_page.checkout()

    checkout_page = CheckoutPage(driver)

    with allure.step("Ввести имя"):
        checkout_page.enter_first_name("Мария")

    with allure.step("Ввести фамилию"):
        checkout_page.enter_last_name("Мардоян")

    with allure.step("Ввести почтовый индекс"):
        checkout_page.enter_postal_code("193079")

    with allure.step("Продолжить оформление заказа"):
        checkout_page.continue_checkout()

    with allure.step("Получить итоговую сумму"):
        total = checkout_page.get_total()
        print(total)

    with allure.step("Проверить итоговую сумму"):
        assert total == 'Total: $58.29'
