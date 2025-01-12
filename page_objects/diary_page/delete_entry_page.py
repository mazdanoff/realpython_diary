from page_objects.diary_page.diary_page import DiaryPage
from web_elements.button import Button
from .delete_entry_page_locators import DeleteEntryPageLocators as Locators


class DeleteEntryPage(DiaryPage):

    confirm = Button(Locators.CONFIRM)
    cancel = Button(Locators.CANCEL)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locators.CONFIRM, timeout=timeout)

    def is_page_displayed(self):
        return self._is_url_correct() and self._is_confirm_delete_displayed()

    def _is_url_correct(self):
        return "delete" in self.driver.current_url

    def _is_confirm_delete_displayed(self):
        return self.is_element_located_displayed(Locators.CONFIRM)
