from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from settings import BASE_URL


class ForgotPasswordPage(BasePage):
    PATH_FORGET_PASSWORD = "/auth/recover-password"

    HINT_FORGET_EMAIL = "Please enter the email address you used to register your account."
    TEXT_BOX_EMAIL = 'input[id="Email"]'
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def open_forget_password(self):
        self.open(self.PATH_FORGET_PASSWORD)

    def forget_password_page_should_be_opened(self):
        self.expect_url(self.PATH_FORGET_PASSWORD)
        expect(
            self.page.get_by_text(self.HINT_FORGET_EMAIL)
        ).to_be_visible()

    def fill_email(self, email: str):
        self.page.fill(self.TEXT_BOX_EMAIL, email)

    def click_btn_send(self):
        (self.page.get_by_role("button", name="Send")
         .click())
