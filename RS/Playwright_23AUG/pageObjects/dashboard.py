from .ordersHistory import OrderHistoryPage

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNaviLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordersHistoryPage = OrderHistoryPage(self.page)
        return ordersHistoryPage



