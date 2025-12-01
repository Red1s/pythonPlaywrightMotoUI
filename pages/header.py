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
        # первый nav считаем верхним хедером
        self.header = self.page.locator("nav").first

    def header_avatar_img(self):
        return self.header.locator("[data-slot='trigger']:has(img[alt='avatar'])")

    def ensure_avatar_circle_is_visible(self):
        expect(self.header_avatar_img().first).to_be_visible()