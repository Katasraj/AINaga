from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture(scope="class")
def init_chrome_driver(request):
    service = Service(ChromeDriverManager().install())
    ch_driver = webdriver.Chrome(service=service)
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.mark.usefixtures('init_chrome_driver')
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"