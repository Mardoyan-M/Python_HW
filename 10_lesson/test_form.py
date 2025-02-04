import pytest
import allure
from selenium import webdriver
from pages.form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тестирование формы")
@allure.description("Проверка заполнения и отправки формы")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_form(driver):
    form_page = FormPage(driver)

    with allure.step("Открытие страницы формы"):
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

    with allure.step("Заполнение формы"):
        form_page.fill_form(form_data)

    with allure.step("Отправка формы"):
        form_page.submit_form()

    for field_id in form_data.keys():
        with allure.step(f"Проверка успешного заполнения поля: {field_id}"):
            assert form_page.is_field_success(field_id)

    with allure.step("Проверка поля 'zip-code' на наличие ошибки"):
        assert form_page.is_field_danger("zip-code")
