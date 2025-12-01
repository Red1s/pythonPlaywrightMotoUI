from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LogInPage(BasePage):
    PATH_LOG_IN = "/auth/login"
    USERNAME_INPUT = 'input[id="Username or email"]'
    PASSWORD_INPUT = 'input[id="Password"]'
    LOGIN_BUTTON = 'button:has-text("Log in now")'
    PASSWORD_EYE_BUTTON = ".text-field_passwordEyeBtn__VMAzz button"
    NO_USER_ERROR = "No user found with that username."
    PASSWORD_INCORRECT = "Entered password is incorrect."

    def open_login(self):
        self.open(self.PATH_LOG_IN)

    def auth(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def should_have_username_label(self):
        expect(self.page.get_by_text("Username or email")).to_be_visible()

    def type_login(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)

    def type_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)

    def should_password_hidden(self):
        expect(self.page.locator(self.PASSWORD_INPUT)).to_have_attribute("type", "password")

    def btm_password_eye(self):
        self.page.locator(self.PASSWORD_EYE_BUTTON).click()

    def should_password_visible(self):
        expect(self.page.locator(self.PASSWORD_INPUT)).to_have_attribute("type", "text")

    def user_exists_in_db(self):
        expect(self.page.get_by_text(self.NO_USER_ERROR)).to_be_visible()

    def password_is_incorrect(self):
        expect(self.page.get_by_text(self.PASSWORD_INCORRECT)).to_be_visible()

    def should_be_opened(self):
        self.expect_url(self.PATH_LOG_IN)
        expect(self.page.get_by_role("button", name="Log in now")).to_be_visible()