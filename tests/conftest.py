from dataclasses import dataclass
from datetime import datetime
from sqlite3 import connect, Error

from pytest import fixture
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions

from conf.paths import geckodriver, database_path


@fixture
def driver():
    options = FirefoxOptions()
    firefox = Firefox(options=options, executable_path=geckodriver)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()




def pytest_addoption(parser):
    parser.addini('username', help='Used to log in to diary')
    parser.addini('password', help='Used to log in to diary')
