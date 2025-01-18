import time

from playwright.sync_api import Page, expect


def test_dynamic_Section_Validation(page : Page):
    # TC: add iphone x and Nokia Edge --> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Student")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name='Sign In').click()

    page.locator("app-card").filter(has_text="iphone X").get_by_role("button").click()
    page.locator("app-card").filter(has_text="Nokia Edge").get_by_role("button").click()
    page.get_by_text("Checkout").click()
    # page.locator(".media-body")
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)