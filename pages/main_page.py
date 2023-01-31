from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    SEARCH = (By.ID, '')

    def tap_search(self):
        self.click(*self.SEARCH)
