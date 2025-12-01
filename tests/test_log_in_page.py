from settings import LOGIN, PASSWORD
from playwright.sync_api import Page
from pages.log_in_page import LogInPage
from pages.header import Header


def test_auth_log_in_success(auth, header):
    auth.open_login()
    auth.auth(LOGIN, PASSWORD)
    header.ensure_avatar_circle_is_visible()

def test_auth_password_is_hidden_by_default(auth):
    auth.open_login()
    auth.type_password(PASSWORD)
    auth.should_password_hidden()

def test_auth_show_password_button(auth):
    auth.open_login()
    auth.type_password(PASSWORD)

    auth.btm_password_eye()
    auth.should_password_visible()

    auth.btm_password_eye()
    auth.should_password_hidden()

def test_auth_wrong_log_in(auth):
    auth.open_login()
    auth.type_login("wronglogin123")
    auth.user_exists_in_db()

def test_auth_correct_log_and_wrong_pass(auth):
    auth.open_login()
    auth.auth(LOGIN, "WrongPassword123")
    auth.password_is_incorrect()


