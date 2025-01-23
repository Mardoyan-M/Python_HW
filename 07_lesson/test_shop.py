import pytest
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


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    product_page = ProductPage(driver)
    product_page.add_to_cart('add-to-cart-sauce-labs-backpack')
    product_page.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    product_page.add_to_cart('add-to-cart-sauce-labs-onesie')
    product_page.go_to_cart()
    product_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("Мария")
    checkout_page.enter_last_name("Мардоян")
    checkout_page.enter_postal_code("193079")
    checkout_page.continue_checkout()

    total = checkout_page.get_total()
    print(total)
    assert total == 'Total: $58.29'
