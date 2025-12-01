from playwright.sync_api import Page, expect
from settings import BASE_URL

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        self.page.goto(f"{BASE_URL}{path}")

    def expect_url(self, path: str):
        expect(self.page).to_have_url(f"{BASE_URL}{path}")