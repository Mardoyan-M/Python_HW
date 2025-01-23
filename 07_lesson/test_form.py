import pytest
from selenium import webdriver
from pages.form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form(driver):
    form_page = FormPage(driver)
    form_page.open()

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    form_page.fill_form(form_data)
    form_page.submit_form()

    for field_id in form_data.keys():
        assert form_page.is_field_success(field_id)

    assert form_page.is_field_danger("zip-code")
