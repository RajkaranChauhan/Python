from playwright.sync_api import Page


def test_web_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    print(page.locator("th").count())
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            rice_column_index = index
            print(f"the Rice column index is : {rice_column_index}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    rice_price = rice_row.locator("td").nth(rice_column_index).text_content()
    print(rice_price)
    assert int(rice_price) == 37
