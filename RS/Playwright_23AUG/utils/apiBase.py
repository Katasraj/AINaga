from playwright.sync_api import Playwright

ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response= api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "naga45@gmail.com", "userPassword": "Katasraj111#"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order", data=ordersPayLoad,
                                 headers={"Authorization":token,
                                          "content-type":"application/json"})
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId