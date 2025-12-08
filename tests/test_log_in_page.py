import pytest

from settings import LOGIN, PASSWORD



# @allure.story("Basic login flow")
# @allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.critical
def test_auth_log_in_success(auth, header):
    auth.open_login()
    auth.auth(LOGIN, PASSWORD)
    header.ensure_avatar_circle_is_visible()

@pytest.mark.smoke
def test_auth_password_is_hidden_by_default(auth):
    auth.open_login()
    auth.type_password(PASSWORD)
    auth.should_password_hidden()

@pytest.mark.sanity
def test_auth_show_password_button(auth):
    auth.open_login()
    auth.type_password(PASSWORD)

    auth.click_btm_password_eye()
    auth.should_password_visible()

    auth.click_btm_password_eye()
    auth.should_password_hidden()

@pytest.mark.sanity
def test_auth_wrong_log_in(auth):
    auth.open_login()
    auth.type_login("wronglogin123")
    auth.user_exists_in_db()

@pytest.mark.sanity
def test_auth_correct_log_and_wrong_pass(auth):
    auth.open_login()
    auth.auth(LOGIN, "WrongPassword123")
    auth.password_is_incorrect()

@pytest.mark.sanity
def test_btn_loginnow_disable(auth):
    auth.open_login()

@pytest.mark.sanity
def test_btn_forgot_password_works(auth, forget_pass):
    auth.open_login()
    auth.click_btn_forgot_password()
    forget_pass.forget_password_page_should_be_opened()

@pytest.mark.smoke
def test_btn_sign_in(auth, sign_up):
    auth.open_login()
    auth.click_btn_sign_in()
    sign_up.sign_in_page_should_be_opened()


