from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class EntryList(DataTable):
    rows_locator = (By.CSS_SELECTOR, "div#entry-list > article")
    date_time = Column(By.CSS_SELECTOR, "article:nth-of-type({row}) > h2")
    title = Column(By.CSS_SELECTOR, "article:nth-of-type({row}) > h3 > a")
