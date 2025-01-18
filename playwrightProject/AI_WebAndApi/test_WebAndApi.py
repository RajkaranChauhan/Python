import time

from playwright.sync_api import Playwright, expect
from apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order -> get order id

    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    # login

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("raj.gamebegins@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Learning1#")
    page.get_by_role("button", name="Login").click()

    # order history page -> order is present
    page.get_by_role("button", name="ORDERS").click()
    order_row = page.locator("tr").filter(has_text=order_id)
    order_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # time.sleep(5)
    context.close()
