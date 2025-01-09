from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():

    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

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

    for field, value in form_data.items():
        driver.find_element(By.CSS_SELECTOR,
                            f"[name={field}]").send_keys(value)

    driver.find_element(By.CSS_SELECTOR,
                        "button[type=submit]").click()

    for field_id in list(form_data.keys()):
        assert ("alert-success" in driver.find_element(
            By.ID, field_id).get_attribute("class"))

    assert ("alert-danger" in driver.find_element(
        By.ID, 'zip-code').get_attribute("class"))

    driver.quit()
