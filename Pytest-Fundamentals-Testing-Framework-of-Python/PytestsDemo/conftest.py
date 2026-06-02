import pytest


@pytest.fixture(scope= "class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture(scope= "class")
def dataload():
    print("user profile data is being created")
    return ["Nagasai", "Thumati", "thumati.nagasai35@gmail.com"]


@pytest.fixture(params= [("Nagasai", "chrome"), "firefox", "Internet Explorer"])
def crossbrowser(request):
    return request.param