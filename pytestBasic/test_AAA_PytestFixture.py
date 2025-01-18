import pytest


# By default scope is function and it will run before all the function in the test file
# scope= mudule : it will run only one time for all the function in the test file
# @pytest.fixture(scope='function')
@pytest.fixture(scope='function')
def pre_work():
    print("PreWork")
    return "function"


def test_FirstTest(pre_work):
    print("First Test")
    print("value returned is: "+pre_work)


def test_SecondTest(pre_work):
    print("Second Test")
    print("value returned is: " + pre_work)


def test_ThirdTest(defaultConfig):  # The fixture of the function is called from conftest.py
    print("Third Test")
    print("value returned is: " + defaultConfig)
