from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


# @pytest.fixture(params=['chrome', 'firefox'], scope="class")
# def init_driver(request):
#     if request.param == "chrome":
#         service = Service(ChromeDriverManager().install())
#         web_driver = webdriver.Chrome(service=service)
#     request.cls.driver = web_driver
#
#     yield
#     web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_test(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

