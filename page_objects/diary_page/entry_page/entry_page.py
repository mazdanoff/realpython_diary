from page_objects.diary_page.diary_page import DiaryPage
from page_objects.diary_page.entry_page.entry_page_locators import EntryPageLocators as Locators
from web_elements.link import Link
from web_elements.text import Text


class EntryPage(DiaryPage):

    date_time = Text(Locators.DATE_TIME)
    title = Text(Locators.TITLE)
    entry_text = Text(Locators.ENTRY_TEXT)

    edit = Link(Locators.EDIT)
    delete = Link(Locators.DELETE)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locators.ENTRY_TEXT)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Locators.ENTRY_TEXT)
