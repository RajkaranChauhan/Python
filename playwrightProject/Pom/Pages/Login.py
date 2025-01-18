import json
import time
from playwright.sync_api import Page
import pytest


class Login():




    def __init__(self, page : Page):
        self.page = page

        print("in login const")
        self.txt_box_user_name = page.get_by_placeholder("email@example.com")
        self.txt_box_pass = page.get_by_placeholder("enter your passsword")
        self.btn_login = page.get_by_role('button', name='Login')

    def navigate_to_application(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login_to_application(self,user,passw):
        self.user = user
        self.passw = passw
        self.txt_box_user_name.fill(self.user)
        self.txt_box_pass.fill(self.passw)
        self.btn_login.click()
        print("login success")