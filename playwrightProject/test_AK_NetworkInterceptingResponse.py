from playwright.sync_api import Page


# api call form browser --> api call contact server--> server give response to browser -> browser display the data as per response
fakePayLoadOrderResponse = {"data": [], "message": "No Orders"}
def intercept_response(route):
    route.fulfill(
        json=fakePayLoadOrderResponse
    )


def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    # login to app --> network tab --> goto order details --> Header
    # Request URL: https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/64ff4f787244490f95ac890e

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("raj.gamebegins@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Learning1#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)