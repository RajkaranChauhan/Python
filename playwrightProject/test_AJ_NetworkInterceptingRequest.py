import time

from playwright.sync_api import Page


# updating the api call form browser with different users orderid and checking the response

# 6771a641e2b5443b1f08c524 is fake order id of different user
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6771a641e2b5443b1f08c524"
    )


def test_network_2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    # login to app --> network tab --> goto order details --> view  --> Header  --> get-order-details
    # Request URL: https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/64ff4f787244490f95ac890e

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("raj.gamebegins@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Learning1#")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click() # right now we are clicking in any view button present in page
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)