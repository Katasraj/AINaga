from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

'''
ChromeDriverManager().install() returns a string path to the ChromeDriver executable, 
but Selenium 4+ no longer accepts a plain string as the first argument to webdriver.Chrome().

Selenium now requires a Service object.
'''

def test_google():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    assert driver.title == "Facebook - log in or sign up"
    driver.quit()

def test_insta():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com")
    assert driver.title == "Gmail"
    driver.quit()

def test_rediff():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.rediff.com")
    assert driver.title == "rediff"
    driver.quit()