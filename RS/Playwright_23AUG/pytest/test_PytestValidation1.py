# import pytest
#
# @pytest.fixture(scope="module")
# def preWork():
#     print("I setup browser instance")


def test_initialCheck(preWork):
    print("This is first test")

def test_SecondCheck(preWork):
    print("This is second test")
