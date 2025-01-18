




def test_func_login(playwright, browser_instance):
    page = browser_instance
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill('raj.gamebegins@gmail.com')
    page.get_by_placeholder("enter your passsword").fill('Learning1#')
    page.get_by_role("button", name="Login").click()
    # loginPage= Login(browser_instance)
    # loginPage.login_to_application('raj.gamebepytestgins@gmail.com','Learning1#')