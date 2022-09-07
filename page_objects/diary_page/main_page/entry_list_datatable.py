from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column

from utils.db_conn_handler import Entry


class EntryList(DataTable):
    rows_locator = (By.CSS_SELECTOR, "div#entry-list > article")
    date_time = Column(By.CSS_SELECTOR, "article:nth-of-type({row}) > h2")
    title = Column(By.CSS_SELECTOR, "article:nth-of-type({row}) > h3 > a")

    def get_entry(self, entry: Entry):
        item = self.get_item_by_property(title=entry.title)
        return item
