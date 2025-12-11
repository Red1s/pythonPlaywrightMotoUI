import pytest
import time

from pages.forgot_password_page import ForgotPasswordPage
from settings import EMAIL_FOR_SEND_TEST

def test_send_reset_password(forget_pass):
    forget_pass.open_forget_password()
    forget_pass.fill_email(EMAIL_FOR_SEND_TEST)
    forget_pass.click_btn_send()
    forget_pass.email_has_been_sent()
    time.sleep(3)

def test_input_incorrect_email(forget_pass):
    forget_pass.open_forget_password()
    forget_pass.fill_email("maildoesnotexist273@gmail.com")
    forget_pass.used_not_exist_is_visible()
    forget_pass.btn_send_disable()

def test_bnt_back_go_to_log_in_page(forget_pass, auth):
    forget_pass.open_forget_password()
    forget_pass.click_btn_back()
    auth.login_page_should_be_opened()

