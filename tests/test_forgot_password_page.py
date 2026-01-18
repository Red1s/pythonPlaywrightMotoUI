import time
import pytest
import allure


from pages.forgot_password_page import ForgotPasswordPage
from settings import EMAIL_FOR_SEND_TEST

@allure.feature("Forgot password")
@allure.story("UI notifies forgot password mail - sent (operates once every 10 minutes)")
def test_send_reset_password(forget_pass):
    '''
    The UI notifies that the email with the password request has been sent
    (operates once every 10 minutes)
    '''
    forget_pass.open_forget_password()
    forget_pass.fill_email(EMAIL_FOR_SEND_TEST)
    forget_pass.click_btn_send()
    forget_pass.mail_has_been_sent_for_forgot_password()

@allure.feature("Forgot password")
@allure.story("The 'Forget password' form notifies the user that the entered username does not exist."
              "And won't let me send the letter")
def test_input_incorrect_email(forget_pass):
    forget_pass.open_forget_password()
    forget_pass.fill_email("maildoesnotexist273@gmail.com")
    forget_pass.used_not_exist_is_visible()
    forget_pass.btn_send_disable()

@allure.feature("Forgot password")
@allure.story("Switching back from the 'Forgot password' tab to 'Log in'")
def test_bnt_back_go_to_log_in_page(forget_pass, auth):
    forget_pass.open_forget_password()
    forget_pass.click_btn_back()
    auth.login_page_should_be_opened()

