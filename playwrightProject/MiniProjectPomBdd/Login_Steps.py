import os

from pytest_bdd import scenarios, given, when, then, parsers

from playwrightProject.MiniProjectPomBdd.LoginPage import LoginPage


# class LoginSteps():
#     def __init__(self,browser_instance):
#         self.page = browser_instance
#         self.loginpage= LoginPage(self.page)
#
# Get the absolute path of the feature file
# script_dir = os.path.dirname(os.path.abspath("."))
# print("------"+script_dir)
# # feature_file_path = os.path.join(script_dir, 'FeatureFiles','Login.feature')
# # print("------"+feature_file_path)
#
# # Call the scenarios function with the correct file path
# scenarios("FeatureFiles/Login.feature")

# print(os.path.exists("D:/Dev/Python/RahulSheetyPlaywrightPython/PlayWrightPython/PyTestPthon/playwrightProject/MiniProjectPomBdd/FeatureFiles/Login.feature"))
# print("****")
# # Get the absolute path of the base directory containing feature files
# script_dir = os.path.dirname(os.path.abspath(__file__))
# features_dir = os.path.join(script_dir, 'FeatureFiles')
#
# # Pass the base directory to scenarios
# boo=os.path.exists(features_dir)
# print("path exists: "+ str(boo))
# scenarios(features_dir)

scenarios("FeatureFiles/Login.feature")

class LoginSteps():
    def __init__(self, browser_instance):
        self.page = browser_instance
        self.loginpage = LoginPage(self.page)

    @given("the login page is displayed")
    def display_login_page(self,browser_instance):
        # login = LoginPage(browser_instance)
        self.loginpage .navigate_to_application()

    @when(parsers.parse("I enter {email} in the email field"))
    def enter_email(context, email):
        context.page.fill("#userEmail", email)

    @when(parsers.parse("I enter {password} in the password field"))
    def enter_password(context, password):
        context.page.fill("#userPassword", password)

    @when("I click on the login button")
    def click_login_button(context):
        context.page.click("#login")

    @then("I should be logged into the application")
    def verify_login(context):
        assert context.page.is_visible("#dashboard"), "Login failed or dashboard not displayed"
        context.browser.close()