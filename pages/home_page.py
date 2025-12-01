from playwright.sync_api import Page, expect
from .base_page import BasePage, BASE_URL
from .log_in_page import LogInPage


class HomePage(BasePage):

    def open_home(self):
        self.open("/")

    def click_log_in_page(self):
        self.page.get_by_role('button', name='Log in').click()
