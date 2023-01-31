from selenium.webdriver.common.by import By

from pages.base_page import Page
class SearchPage(Page):
    SEARCH_FIELD = (By.ID, '')
    SEARCH_RESULT = (By.ID, '')

    def input_search(self, search_phrase: str):
        self.input(search_phrase, *self.SEARCH_FIELD)

    def verify_search_result(self, search_phrase: str):
        result_text = self.find_element(*self.SEARCH_RESULT).text
        assert search_phrase in result_text, f'not found in {search_phrase}'