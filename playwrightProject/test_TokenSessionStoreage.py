import time

from playwright.sync_api import expect
from playwright.sync_api import Playwright

from AI_WebAndApi.apiBase import APIUtils


# making api call to login --> fetching session from local storage
# --> passing it on UI browser to by pass user loign and perform some acitons

def test_token_session_local_storage(playwright : Playwright):
    api_utils = APIUtils()
    token = api_utils.get_token(playwright)
    print(token)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # java script in triple quote
    page.add_init_script(f"""localStorage.setItem("token","{token}")""")
    page.goto("https://rahulshettyacademy.com/client")
    # it should by pass login screen
    # time.sleep(3)
    page.get_by_role("button", name="ORDERS").click()
    # time.sleep(3)
    expect(page.get_by_text('Your Orders')).to_be_visible()