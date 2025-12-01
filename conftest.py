import pytest

from settings import LOGIN, PASSWORD
from pages.log_in_page import LogInPage
from pages.header import Header
from pages.home_page import HomePage


@pytest.fixture
def auth(page):
    return LogInPage(page)

@pytest.fixture
def home(page):
    return HomePage(page)

@pytest.fixture
def header(page):
    return Header(page)

@pytest.fixture
def logged_in_user(page):
    login = LogInPage(page)
    login.open_login()
    login.auth(LOGIN, PASSWORD)
    return Header(page)
