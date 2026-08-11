import pytest

@pytest.mark.login
def test_m1():
    a = 5
    b = 3
    assert b+2 == a, "test passed"
    assert a+1 == b, "test failed as a is not equal to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True

def test_m4():
    assert False

@pytest.mark.login
def test_m5():
    assert 100 == 100

def test_m6():
    assert "naga" == "NAGA"

@pytest.mark.login
def test_login_FB():
    assert "admin" == "admin1"


