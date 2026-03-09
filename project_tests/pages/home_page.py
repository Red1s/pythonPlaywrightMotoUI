from playwright.sync_api import Page, expect
from .base_page import BasePage, BASE_URL
from .log_in_page import LogInPage


class HomePage(BasePage):

    def open_home(self):
        self.open("/")
