import pytest
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions

from conf.paths import GECKODRIVER


@pytest.fixture
def driver():
    options = FirefoxOptions()
    firefox = Firefox(options=options, executable_path=GECKODRIVER)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()
