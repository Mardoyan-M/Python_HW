from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

waiter = WebDriverWait(driver, 10)

first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
first_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
last_name.send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
address.send_keys("Ленина, 55-3")

email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
email.send_keys("test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
phone.send_keys("+7985899998787")

city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
city.send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
country.send_keys("Россия")

job = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
job.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
company.send_keys("QA")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

waiter = WebDriverWait(driver, 20)

assert "danger" in driver.find_element(
    By.ID, "zip-code").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "first-name").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "last-name").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "address").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "e-mail").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "phone").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "city").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "country").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "job-position").get_attribute("class")

assert "success" in driver.find_element(
    By.ID, "company").get_attribute("class")


driver.quit()
