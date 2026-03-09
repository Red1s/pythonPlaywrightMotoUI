import os
import re
import pytest
import allure
from playwright.sync_api import Page
from config.settings import LOGIN, PASSWORD
from project_tests.pages.forgot_password_page import ForgotPasswordPage
from project_tests.pages.log_in_page import LogInPage
from project_tests.pages.sign_in_page import SignUpPage
from project_tests.pages.header import Header
from project_tests.pages.home_page import HomePage


@pytest.fixture
def auth(page):
    return LogInPage(page)


@pytest.fixture
def sign_up(page):
    return SignUpPage(page)


@pytest.fixture
def home(page):
    return HomePage(page)


@pytest.fixture
def header(page):
    return Header(page)


@pytest.fixture
def forget_pass(page):
    return ForgotPasswordPage(page)


@pytest.fixture
def logged_in_user(auth):
    auth.login_user(LOGIN, PASSWORD)


# ------ Если тест падает: делаем скрин в Allure И прикрепляем отчет trace.zip из "Playwright Trace Viewer" ------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # 1. Запоминаем, упал ли тест на этапе выполнения (call)
    if report.when == "call":
        item.test_failed = report.failed

    # 2. Этап CALL: Тест упал -> Делаем скриншот (пока браузер еще открыт)
    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )

    # 3. Этап TEARDOWN: Контекст закрыт -> Ищем trace.zip и прикрепляем в Allure вместе с инструкцией
    if report.when == "teardown" and getattr(item, "test_failed", False):
        test_results_dir = "test-results"

        # Очищаем имя теста от спецсимволов, чтобы оно совпало с названием папки Playwright
        test_func_name = item.name
        safe_test_name = re.sub(r'[^a-zA-Z0-9]', '-', test_func_name)
        safe_test_name = re.sub(r'-+', '-', safe_test_name).strip('-')

        if os.path.exists(test_results_dir):
            # Ищем папки, относящиеся к нашему упавшему тесту
            matching_folders = [
                os.path.join(test_results_dir, d)
                for d in os.listdir(test_results_dir)
                if os.path.isdir(os.path.join(test_results_dir, d)) and safe_test_name in d
            ]

            if matching_folders:
                # Берем самую свежую папку (от текущего прогона)
                latest_folder = max(matching_folders, key=os.path.getmtime)
                trace_path = os.path.join(latest_folder, "trace.zip")

                # Если архив физически существует на диске
                if os.path.exists(trace_path):
                    # Прикрепляем сам архив
                    allure.attach.file(
                        trace_path,
                        name=f"Playwright Trace",
                        attachment_type="application/zip",
                        extension=".zip"
                    )

                    # Прикрепляем кликабельную ссылку и мини-инструкцию
                    html_instruction = """
                    <div style="font-family: Arial, sans-serif; padding: 10px; border: 1px solid #d0d0d0; border-radius: 5px; background-color: #f9f9f9;">
                        <h4 style="margin-top: 0;">🛠 Как посмотреть этот Trace:</h4>
                        <ol style="margin-bottom: 0;">
                            <li>Скачайте архив <b>Playwright Trace</b> (кнопка выше).</li>
                            <li>Откройте официальный плеер: <b><a href="https://trace.playwright.dev/" target="_blank">trace.playwright.dev</a></b></li>
                            <li>Перетащите скачанный zip-архив прямо в окно браузера.</li>
                        </ol>
                    </div>
                    """
                    allure.attach(
                        html_instruction,
                        name="📖 Инструкция: Как открыть Trace",
                        attachment_type=allure.attachment_type.HTML
                    )