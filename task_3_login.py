import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_login_admin():
    driver = webdriver.Chrome()
    driver.get("http://localhost/litecart/admin/")
    username = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    username.send_keys("admin")
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password.send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
    time.sleep(5)
    driver.quit()
