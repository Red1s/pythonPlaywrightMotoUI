from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from settings import BASE_URL


class ForgotPasswordPage(BasePage):
    PATH_FORGET_PASSWORD = "/auth/recover-password"

    HINT_FORGET_EMAIL = "Please enter the email address you used to register your account."
    TEXT_BOX_EMAIL = "input[id='Email']"
    TEXT_USER_NOT_EXIST = "The value used does not exist"
    TEXT_BTN_SEND = "Send"
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
        expect(self.page.get_by_role('button', name=self.TEXT_BTN_SEND)).to_be_enabled()
        self.page.get_by_role("button", name=self.TEXT_BTN_SEND).click()

    def email_has_been_sent(self):
        expect(self.page.get_by_text("The email has been sent")).to_be_visible()

    def used_not_exist_is_visible(self):
        expect(self.page.get_by_text(self.TEXT_USER_NOT_EXIST)).to_be_visible()

    def btn_send_disable(self):
        expect(self.page.get_by_role('button', name=self.TEXT_BTN_SEND)).to_be_disabled()

    def click_btn_back(self):
        self.page.get_by_role("link", name="Back").click()

