import allure
from playwright.sync_api import expect
from .base_page import BASE_URL, BasePage

class Header(BasePage):
    HOME_TAB = ("link", "HOME")
    VIDEOS_TAB = ("link", "VIDEOS")
    EXPLORE_TAB = ("link", "EXPLORE")
    SEARCH_TAB = ()
    INTERACTIONS_TAB = ()
    CHAT_TAB = ()
    SING_UP_TAB = ("link", "Sing up")
    LOG_IN_TAB = ("link", "Sing in")

    def __init__(self, page):
        super().__init__(page)
        # We consider the first nav to be the top header
        self.header = self.page.locator("nav").first

    #methods-locators
    @allure.step("returns the locator of the avatar object")
    def header_avatar_img(self):
        return self.header.locator("[data-slot='trigger']:has(img[alt='avatar'])")

    @allure.step("The user's avatar is displayed in the Header")
    def ensure_avatar_circle_is_visible(self):
        expect(self.header_avatar_img().first).to_be_visible()

    @allure.step("Клик по кнопке 'Log in' in Header")
    def click_log_in_page(self):
        self.page.get_by_role('button', name='Log in').click()