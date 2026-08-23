import pytest

@pytest.fixture(scope="session")
def preSetupWork():
    print("I setup browser instance")


@pytest.fixture(scope="module")
def preWork():
    print("I setup browser module instance")
