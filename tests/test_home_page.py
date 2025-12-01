from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.log_in_page import LogInPage



def test_auth_page_check(auth, header):

    header.open_home()
    header.click_log_in_page()
    auth.should_have_username_label()


