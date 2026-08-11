import pytest

def test_m1():
    a = 5
    b = 3
    assert b+2 == a, "test passed"
    assert a+1 == b, "test failed as a is not equal to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

def test_m3():
    assert True

def test_login_Insta():
    assert "admin" == "admin"