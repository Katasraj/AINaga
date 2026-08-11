import pytest

def test_m4():
    assert False

@pytest.mark.home
def test_m5():
    assert 100 == 100

def test_m6():
    assert "naga" == "NAGA"

@pytest.mark.home
def test_login_Gmail():
    assert "admin" == "admin"
