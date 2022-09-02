from abc import abstractmethod

from page_objects.abstract.abs_page_object import AbsPageObject


class UrlException(Exception):
    pass


class AbsBasePage(AbsPageObject):

    def __init__(self, driver, url: str = None):
        super(AbsBasePage, self).__init__(driver)
        self.url = url

    def open(self, url: str = None):
        url = url or self.url
        if not url:
            raise UrlException("Page URL is not provided")
        self.driver.get(url)
        return self

    @abstractmethod
    def is_page_displayed(self):
        pass

    @abstractmethod
    def wait_for_page_to_load(self, timeout: int):
        pass
