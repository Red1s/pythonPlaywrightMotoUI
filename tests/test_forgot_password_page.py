import pytest
import time

from pages.forgot_password_page import ForgotPasswordPage
from settings import EMAIL_FOR_SEND_TEST

def test_send_reset_password(forget_pass):
    forget_pass.open_forget_password()
    forget_pass.fill_email(EMAIL_FOR_SEND_TEST)
    forget_pass.click_btn_send()
    time.sleep(3)