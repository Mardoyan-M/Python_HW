from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

options = webdriver.FirefoxOptions()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

field_username = driver.find_element(By.ID, "username")
field_username.send_keys("tomsmith")

field_password = driver.find_element(By.ID, "password")
field_password.send_keys("SuperSecretPassword!")

button_login = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit']").click()

sleep(5)
driver.quit()
