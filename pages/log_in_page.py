import allure

from playwright.sync_api import Page, expect
from pages.base_page import BasePage



class LogInPage(BasePage):
    PATH_LOG_IN = "/auth/login"

    #locators
    USERNAME_PLACEHOLDER = 'Enter the user name or email'
    PASSWORD_PLACEHOLDER = 'Enter your account password'
    LOGIN_BUTTON = 'button:has-text("Log in now")'

    NO_USER_ERROR = "No user found with that username."
    PASSWORD_INCORRECT = "Entered password is incorrect."

    # methods-locators
    def username_field(self):
        return self.page.get_by_placeholder(self.USERNAME_PLACEHOLDER)

    def password_field(self):
        return self.page.get_by_placeholder(self.PASSWORD_PLACEHOLDER)

    def password_eye_button(self):
        # 1. xPath We go up to the password field container
        container = self.password_field().locator("xpath=ancestor::div[1]")
        # 2 CSS Inside the container, we find the peephole button.
        return container.locator("css=div[class*='passwordEyeBtn'] button")

    # methods
    @allure.step("Open login page")
    def open_login(self):
        self.open(self.PATH_LOG_IN)

    @allure.step("The user has logged in")
    def auth(self, username: str, password: str):
        self.username_field().fill(username)
        self.password_field().fill(password)
        self.page.click(self.LOGIN_BUTTON)

    @allure.step("PRECONDITION: user is logged in")
    def login_user(self, username: str, password: str):
        self.open_login()
        self.auth(username, password)

    @allure.step("Enter the specified login")
    def type_login(self, username: str):
        self.username_field().fill(username)

    @allure.step("Enter the password of an existing test user")
    def type_password(self, password: str):
        self.password_field().fill(password)

    @allure.step("Verify that the password is hidden")
    def should_password_hidden(self):
        expect(self.password_field()).to_have_attribute("type", "password")

    @allure.step("Click on the show/hide password button")
    def click_btm_password_eye(self):
        self.password_eye_button().click()

    @allure.step("Verify that the password is visible")
    def should_password_visible(self):
        expect(self.password_field()).to_have_attribute("type", "text")

    @allure.step("UI prompt indicating that such a user does not exist")
    def user_exists_in_db(self):
        expect(self.page.get_by_text(self.NO_USER_ERROR)).to_be_visible()

    @allure.step("UI prompt indicating that the user's password is incorrect")
    def password_is_incorrect(self):
        expect(self.page.get_by_text(self.PASSWORD_INCORRECT)).to_be_visible()

    @allure.step("Verification URL and UI")
    def login_page_should_be_opened(self):
        self.expect_url(self.PATH_LOG_IN)
        with allure.step("And additional verification on the UI (Looking for the button 'Log in now')"):
            expect(self.page.get_by_role("button", name="Log in now")).to_be_visible()

    @allure.step("Press the button 'Forgot the password?' on the page 'Log in'")
    def click_btn_forgot_password(self):
        self.page.locator("a[href='/auth/recover-password']").click()

    @allure.step("Press the button 'Sing up?' on the page 'Log in'")
    def click_btn_sign_in(self):
        self.page.locator("a[href='/auth/register']").click()
