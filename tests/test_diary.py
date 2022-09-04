from hamcrest import assert_that

from page_objects.diary_page.entry_page.entry_page import EntryPage
from page_objects.diary_page.main_page.main_page import MainPage


def test_entry_display(login_session, driver):
    main_page = MainPage(driver)
    entry = main_page.entry_list.get_item_by_property(title="LOOKING FOR A JOB")
    title = getattr(entry, 'title')
    title.click()

    entry_page = EntryPage(driver)
    entry_page.wait_for_page_to_load(5)
    assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
    assert_that(entry_page.entry_text.value == "I need to feed my fellow geese.", "Entry page is not displayed")
