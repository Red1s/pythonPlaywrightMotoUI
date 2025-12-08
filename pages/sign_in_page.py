from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from settings import BASE_URL


class SignUpPage(BasePage):
    PATH_SIGN_UP = "/auth/register"

    TEXT_BOX_EMAIL = 'input[id="Email"]'
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def sign_in_page_should_be_opened(self):
        self.expect_url(self.PATH_SIGN_UP)
        expect(
            self.page.get_by_role("button", name="Sign up now")
        ).to_be_visible()