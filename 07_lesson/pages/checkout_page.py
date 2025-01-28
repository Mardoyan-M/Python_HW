from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(
            By.CSS_SELECTOR, '[name="firstName"]')
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element(
            By.CSS_SELECTOR, '[name="lastName"]')
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        postal_code_field = self.driver.find_element(
            By.CSS_SELECTOR, '[name="postalCode"]')
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(By.ID, 'continue').click()

    def get_total(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
