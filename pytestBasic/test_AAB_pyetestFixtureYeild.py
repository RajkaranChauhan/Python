import pytest


@pytest.fixture(scope='function')
def fix_one():
    print("fixerone")
    return "fix_one returned"


@pytest.fixture(scope='function')
def fix_two():
    print("fixertwo")
    return "fix_two returned"



@pytest.fixture(scope='function')
def fix_yield():
    print("yield before")
    yield
    print("yield after")


def test_function_one(fix_one,fix_two):
    print("function one")
    print(fix_one)
    print(fix_two)

@pytest.mark.skip
def test_function_two(fix_two,fix_yield):
    print("function two")
    print(fix_two)


@pytest.mark.smoke
def test_function_three(fix_one,fix_two):
    print("function three")
    print(fix_one)
    print(fix_two)