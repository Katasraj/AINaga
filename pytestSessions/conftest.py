from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def input_total():
    total = 100
    return total

@pytest.fixture(params=['chrome', 'firefox'], scope="class")
def init_driver(request):
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service)
    request.cls.driver = web_driver

    yield
    web_driver.close()