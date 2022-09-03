from page_objects.abstract.abs_base_page import AbsBasePage
from page_objects.diary_page.diary_page_locators import DiaryPageLocators


class DiaryPage(AbsBasePage):

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(DiaryPageLocators.PAGE_HEADER, timeout=timeout)

    def is_page_displayed(self):
        return self.is_element_located_displayed(DiaryPageLocators.PAGE_HEADER)
