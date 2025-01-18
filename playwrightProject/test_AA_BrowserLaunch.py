import time

from playwright.sync_api import Page, expect, Playwright

'''

def test_browser_launch(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")


def test_playwright_page_mode(page: Page):
    page.goto("https://google.com")
    print("browser launched in page mood")

'''
def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Student")
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button",name='Sign In').click()
    # Empty username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


def test_firefox(playwright : Playwright):
    firefox_browser = playwright.firefox.launch(headless=False)
    context = firefox_browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Student")
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button",name='Sign In').click()
    # Empty username/password.
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)