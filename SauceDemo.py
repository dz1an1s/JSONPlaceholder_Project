from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://www.saucedemo.com/')

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')

    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click()

    time.sleep(2)

    assert "Swag Labs" in driver.title

    print("Тест прошел успешно: вход выполнен!")

except AssertionError:
    print("Тест не прошел: вход не выполнен.")

finally:
    driver.quit()