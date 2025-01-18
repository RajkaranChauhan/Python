from playwright.sync_api import Page, expect


def test_iframe(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    # below for the frame locator is used for the complete body of the iframe and in that we are searching
    #  the test as "Happy Subscibers"
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")
