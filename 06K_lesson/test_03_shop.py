from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

user_name = driver.find_element(By.CSS_SELECTOR, '[name="user-name"]')
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
password.send_keys("secret_sauce")

driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

driver.find_element(By.ID, 'checkout').click()

first_name = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
first_name.clear
first_name.send_keys("Мария")

last_name = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
last_name.clear
last_name.send_keys("Мардоян")

postalcode = driver.find_element(By.CSS_SELECTOR, '[name="postalCode"]')
postalcode.clear
postalcode.send_keys("193079")

driver.find_element(By.ID, 'continue').click()

total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
print(total)
assert total == 'Total: $58.29'
