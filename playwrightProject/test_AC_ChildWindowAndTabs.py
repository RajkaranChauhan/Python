import time

from playwright.sync_api import Page


def test_child_window_and_tab(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:
        page.get_by_text("Free Access to").click()
        # page.locator(".blinkingText").click()
        new_tab = new_page_info.value
        text = new_tab.locator(".im-para.red").text_content()
        print(text)
        words = text.split("at ")
        print(words)
        word = words[1].split(" with")
        email = word[0]
        print("The email address is : "+email)
        assert email == "mentor@rahulshettyacademy.com"
        # time.sleep(5)

