from selenium.webdriver.remote.webdriver import WebDriver  # для подсказок после (.) точки
from selenium.webdriver.support.ui import WebDriverWait  # ← ДОБАВЬТЕ ИМПОРТ


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None


    def __init__(self, driver: WebDriver):  # здесь запрашиваем драйвер на вход на страницу для всех классов
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not opened this page class')


    '''для поиска одного элемента'''
    def find(self, locator: tuple):  # сюда приходит кортеж с методом driver.find_element
        return self.driver.find_element(*locator)  # * распаковывает кортеж


    '''для поиска многих элемента'''
    def find_all(self, locator: tuple):  # сюда приходит кортеж с методом driver.find_element
        return self.driver.find_elements(*locator)  # * распаковывает кортеж

