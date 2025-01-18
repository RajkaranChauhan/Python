from playwright.sync_api import Page


class Dash_Board():

    def __init__(self, page: Page):
        self.page = page
        self.btn_Orders = page.get_by_role("button", name='ORDERS')
        self.text = page.get_by_text('Your Orders')

    def user_clicks_Orders(self):
        self.btn_Orders.click()
        print("orders clicked")
        print(self.text.text_content())