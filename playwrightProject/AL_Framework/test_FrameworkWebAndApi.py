import json
import os
import time

import pytest
from playwright.sync_api import Playwright, expect

from apiBase1 import APIUtils

# json file --> util--> access data
def user_credentials_list():
    # with open('data/credentials.json') as f:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'data', 'credentials.json')
    with open(file_path) as f:
    # with open(r'D:\Dev\Python\RahulSheetyPlaywrightPython\PlayWrightPython\PyTestPthon\playwright\AL_Framework\data\credentials.json') as f:

        test_data=json.load(f)
        print("------>")
        print(test_data)
        return test_data["user_credentials"]

@pytest.mark.parametrize('user_credentials',user_credentials_list())
def test_e2e_web_api(playwright: Playwright,user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    # create order -> get order id

    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    # login

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credentials['email'])
    page.get_by_placeholder("enter your passsword").fill(user_credentials['pass'])
    page.get_by_role("button", name="Login").click()

    # order history page -> order is present
    page.get_by_role("button", name="ORDERS").click()
    order_row = page.locator("tr").filter(has_text=order_id)
    order_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # time.sleep(5)
    context.close()
