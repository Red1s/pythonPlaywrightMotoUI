import pytest
import allure
from playwright.sync_api import Page
from pages.header import Header

@allure.feature("Login")
@allure.story("From the HOME tab, the 'Login in' button will redirect you to the 'Log in' form")
@pytest.mark.smoke
def test_auth_page_check(auth, home, header):
    home.open_home()
    header.click_log_in_page()
    auth.login_page_should_be_opened()

@allure.feature("Header")
@allure.story("The user was able to log in (the avatar is visible in the top right corner)")
@pytest.mark.smoke
def test_avatar_visible(logged_in_user, header):
    header.ensure_avatar_circle_is_visible()

