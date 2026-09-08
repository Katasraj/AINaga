import json

import pytest
from playwright.sync_api import Playwright,expect

from RS.Playwright_23AUG.utils.apiBase import APIUtils
from RS.Playwright_23AUG.pageObjects.login import LoginPage
from RS.Playwright_23AUG.pageObjects.dashboard import DashboardPage

"""load is the method which will convert json into python object"""
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright:Playwright,user_credentials):
    usrName = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    """create order -> orderId"""
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    """Login"""
    loginpage = LoginPage(page)
    loginpage.navigate()
    dashboardPage = loginpage.login(usrName,password)

    # page.goto("https://rahulshettyacademy.com/client/")
    # page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
    # page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    # page.get_by_role("button",name="Login").click()

    # page.get_by_role("button",name="ORDERS").click()

    #Dashboard Page
    orderHistoryPage = dashboardPage.selectOrdersNaviLink()
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)
    ordersDetailsPage.verifyOrderMessage()
    """Verify Order present in history"""
    # row = page.locator("tr").filter(has_text=orderId)
    # row.get_by_role("button",name="View").click()

    # expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
