import pytest

from settings import LOGIN, PASSWORD
from pages.forgot_password_page import ForgotPasswordPage
from pages.log_in_page import LogInPage
from pages.sign_in_page import SignUpPage
from pages.header import Header
from pages.home_page import HomePage


@pytest.fixture
def auth(page):
    return LogInPage(page)

@pytest.fixture
def sign_up(page):
    return SignUpPage(page)

@pytest.fixture
def home(page):
    return HomePage(page)

@pytest.fixture
def header(page):
    return Header(page)

@pytest.fixture
def forget_pass(page):
    return ForgotPasswordPage(page)

@pytest.fixture
def logged_in_user(page):
    login = LogInPage(page)
    login.open_login()
    login.auth(LOGIN, PASSWORD)
    return Header(page)
