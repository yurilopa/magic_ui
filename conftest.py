from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
# from time import sleep  # для запуска in pycharm
from pages.cart_page import CartPage
from pages.cart_page_text import CartPageText
from pages.desk1_page_visibility import Desk1PageVisibility
from pages.desk1_page_text import Desk1PageText
from pages.office_software_visibility import OfficeSoftwareVisibility
from pages.office_software_text import OfficeSoftwareText
from pages.all_page import HeaderPage
from pages.all_page_text import AllPageText


'''**Фикстура `driver`** создает браузер Chrome'''
@pytest.fixture()
def driver():
    options = Options()  # для запуска на сервере
    options.add_argument("--headless")  # для запуска на сервере
    options.add_argument("--no-sandbox")  # для запуска на сервере
    options.add_argument("--disable-dev-shm-usage")  # для запуска на сервере
    options.add_argument("--window-size=1920,1080")  # для запуска на сервере ДОБАВЛЕНО: фиксированный размер окна
    chrome_driver = webdriver.Chrome(options=options)  # для запуска на сервере
    # chrome_driver = webdriver.Chrome()  # для запуска in pycharm
    # sleep(3)  # для запуска in pycharm
    yield chrome_driver  # ← Передаем драйвер в тест
    chrome_driver.delete_all_cookies()
    chrome_driver.quit()  # После теста закрываем браузер


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture()
def cart_page_text(driver):
    return CartPageText(driver)


@pytest.fixture
def desk1_page_visibility(driver):
    """Фикстура для тестов видимости элементов"""
    return Desk1PageVisibility(driver)

@pytest.fixture
def desk1_page_text(driver):
    """Фикстура для тестов текста элементов"""
    return Desk1PageText(driver)


@pytest.fixture
def office_software_visibility(driver):
    """Фикстура для тестов видимости элементов"""
    return OfficeSoftwareVisibility(driver)

@pytest.fixture
def office_software_text(driver):
    """Фикстура для тестов текста элементов"""
    return OfficeSoftwareText(driver)


@pytest.fixture
def all_page_visibility(driver):
    """Фикстура для тестов видимости элементов"""
    return HeaderPage(driver)

@pytest.fixture
def all_page_text(driver):
    """Фикстура для тестов текста элементов"""
    return AllPageText(driver)

