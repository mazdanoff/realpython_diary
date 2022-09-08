from pytest import fixture
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions

from conf.paths import geckodriver
from utils.db_conn_handler import DatabaseConnectionHandler


@fixture
def driver():
    options = FirefoxOptions()
    firefox = Firefox(options=options, executable_path=geckodriver)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()


@fixture
def database():
    db_conn_handler = DatabaseConnectionHandler()
    yield db_conn_handler


def pytest_addoption(parser):
    parser.addini('username', help='Used to log in to diary')
    parser.addini('password', help='Used to log in to diary')
