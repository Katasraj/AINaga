from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None

def setup_module():
    global driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    driver.get("http://www.google.com")

def teardown_module():
    driver.quit()


def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "google.com"

