from page_objects.diary_page.diary_page import DiaryPage
from page_objects.diary_page.main_page.entry_list_datatable import EntryList
from page_objects.diary_page.main_page.main_page_locators import MainPageLocators as Locators
from web_elements.button import Button


class MainPage(DiaryPage):

    entry_list = EntryList(*Locators.ENTRY_LIST)
    add_new_entry = Button(Locators.ADD_NEW_ENTRY)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locators.ADD_NEW_ENTRY)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Locators.ADD_NEW_ENTRY)
