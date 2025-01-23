from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, form_data):
        for field, value in form_data.items():
            self.driver.find_element(
                By.CSS_SELECTOR, f"[name={field}]").send_keys(value)

    def submit_form(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    def is_field_success(self, field_id):
        return "alert-success" in self.driver.find_element(
            By.ID, field_id).get_attribute("class")

    def is_field_danger(self, field_id):
        return "alert-danger" in self.driver.find_element(
            By.ID, field_id).get_attribute("class")
