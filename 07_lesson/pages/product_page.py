from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    def checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()
