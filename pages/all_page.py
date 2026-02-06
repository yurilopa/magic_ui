from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from pages.locators.all_page_locators import AllPageLocators as loc


class HeaderPage(BasePage):
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page URL not defined')


    def find(self, locator: tuple):
        return self.driver.find_element(*locator)


    # === МЕТОДЫ ПРОВЕРКИ HEADER ===
    def is_logo_visible(self):
        """Проверяет видимость логотипа"""
        try:
            logo = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.LOGO)
            )
            return logo.is_displayed()
        except:
            return False


    def is_sign_in_button_visible(self):
        """Проверяет видимость кнопки Sign in"""
        try:
            btn = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.SIGN_IN_BUTTON)
            )
            return btn.is_displayed()
        except:
            return False


    def is_cart_icon_visible(self):
        """Проверяет видимость иконки корзины"""
        try:
            cart = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.CART_ICON)
            )
            return cart.is_displayed()
        except:
            return False


    def is_search_icon_visible(self):
        """Проверяет видимость поиска"""
        try:
            search = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.SEARCH_ICON)
            )
            return search.is_displayed()
        except:
            return False


    # === МЕТОДЫ ПРОВЕРКИ FOOTER ===
    def scroll_to_footer(self):
        """Прокручивает страницу до футера"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        import time
        time.sleep(0.3)


    def is_copyright_visible(self):
        """Проверяет видимость Copyright"""
        try:
            copyright = self.driver.find_element(*loc.COPYRIGHT)
            return copyright.is_displayed()
        except:
            return False


    def is_about_us_visible(self):
        """Проверяет видимость заголовка About us"""
        try:
            about = self.driver.find_element(*loc.ABOUT_US)
            return about.is_displayed()
        except:
            return False


    def is_powered_by_odoo_visible(self):
        """Проверяет видимость ссылки Powered by Odoo"""
        try:
            powered = self.driver.find_element(*loc.POWERED_BY_ODOO)
            return powered.is_displayed()
        except:
            return False
