from playwright.sync_api import Playwright

order_payload = {"orders": [{"country": "India", "productOrderedId": "6519304e7244490f95bf53f2"}]}


class APIUtils():

    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data = {"userEmail": "raj.gamebegins@gmail.com",
                                                    "userPassword": "Learning1#"}
                                            )
        assert response.ok
        response_body = response.json()
        print(response_body)
        token =response_body["token"]
        return token

    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization": token,
                                          "Content-type": "application/json"
                                          }
                                 )
        response_body =response.json()
        print(response_body)
        order_id = response_body["orders"][0] # since order id is in form of list
        # 'orders': ['6771988ae2b5443b1f08b60d'] hence [0] is used to get the data from first index
        return order_id