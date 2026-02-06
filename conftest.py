from selenium import webdriver
import pytest
from time import sleep
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
    chrome_driver = webdriver.Chrome()
    sleep(3)
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

