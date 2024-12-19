from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

options = webdriver.FirefoxOptions()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

driver.find_element(By.CLASS_NAME, 'modal-footer').click()

sleep(5)
driver.quit()
