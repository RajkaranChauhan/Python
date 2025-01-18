import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='module')
def defaultConfig():
    print("Conftest fixture module")
    return "module"


@pytest.fixture(scope='session')
def defaultConfigSession():
    print("Conftest fixture session")
    return "session"


@pytest.fixture(scope='session')
def load_test_data(request):
    return request.param


#########################################

# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")
#
#
# @pytest.fixture()
# def browser_instance(playwright: Playwright, request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         browser = playwright.chromium.launch(headless=False)
#     elif browser_name == "firefox":
#         browser = playwright.firefox.launch(headless=False)
#
#     context = browser.new_context()
#     page = context.new_page()
#     yield page # return page thorough it
#     context.close()
#     browser.close()

