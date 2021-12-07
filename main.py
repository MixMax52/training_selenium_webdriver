import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_open_site():
    driver = webdriver.Chrome()
    driver.get("https://itvdn.com/ru")
    time.sleep(5)
    driver.quit()
