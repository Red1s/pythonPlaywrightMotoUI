import allure
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
        with allure.step(f"And additional verification on the UI (Looking for the text {self.HINT_FORGET_EMAIL}"):
            expect(
                self.page.get_by_text(self.HINT_FORGET_EMAIL)
            ).to_be_visible()

    @allure.step("Returns a Playwright Locator for the email input")
    def email_input(self):
        return self.page.locator(self.TEXT_BOX_EMAIL)

    @allure.step("Fill email field in page 'Forgot password'")
    def fill_email(self, email: str):
        self.email_input().fill(email)

    @allure.step("Click on the active 'Send' button")
    def click_btn_send(self):
        with allure.step("Check that the 'Send' button is active and ready to be clicked"):
            expect(self.page.get_by_role('button', name=self.TEXT_BTN_SEND)).to_be_enabled()
        with allure.step("Press the 'Send' button"):
            self.page.get_by_role("button", name=self.TEXT_BTN_SEND).click()

    @allure.step("UI forgot password approves: 'The email has been sent'")
    def mail_has_been_sent_for_forgot_password(self):
        expect(self.page.get_by_text("The email has been sent")).to_be_visible()

    @allure.step("We see a notification that this user does not exist"
                 " and cannot be sent a password recovery email")
    def used_not_exist_is_visible(self):
        expect(self.page.get_by_text(self.TEXT_USER_NOT_EXIST)).to_be_visible()

    @allure.step("Check that the 'Send' button is active and ready to be clicked")
    def btn_send_disable(self):
        expect(self.page.get_by_role('button', name=self.TEXT_BTN_SEND)).to_be_disabled()

    @allure.step("Press the button 'Back'")
    def click_btn_back(self):
        self.page.get_by_role("link", name="Back").click()
