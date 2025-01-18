import json
import os

import pytest
from playwright.sync_api import Playwright
from playwright.sync_api import Page

from Pages.Dash_Board import Dash_Board
from Pages.Login import Login

# json file --> util--> access data
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data', 'credentials.json')
with open(file_path) as f:
# with open('data/credentials.json') as f:
    test_data = json.load(f)
    print("------>")
    print(test_data)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_init_browser(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    print(user_credentials['email'])
    print(user_credentials['pass'])

    login = Login(page)
    dash_Board = Dash_Board(page)

    login.navigate_to_application()
    login.login_to_application(user_credentials['email'], user_credentials['pass'])
    dash_Board.user_clicks_Orders()