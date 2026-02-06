from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from pages.locators.all_page_locators import AllPageLocators as loc


class AllPageText(BasePage):
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_page(self):
        """Открывает базовый URL"""
        self.driver.get(self.base_url)


    def find(self, locator: tuple):
        return self.driver.find_element(*locator)


    # === МЕТОДЫ ПРОВЕРКИ ТЕКСТА HEADER ===
    def get_categories_text(self):
        """Получает текст кнопки Categories"""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.CATEGORIES)
            )
            return element.text
        except:
            return None


    def get_phone_number_text(self):
        """Получает текст номера телефона"""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.PHONE_NUMBER)
            )
            return element.text
        except:
            return None


    def get_sign_in_button_text(self):
        """Получает текст кнопки Sign in"""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.SIGN_IN_BUTTON)
            )
            return element.text
        except:
            return None


    def get_contact_us_button_text(self):
        """Получает текст кнопки Contact Us"""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(loc.CONTACT_US_BUTTON)
            )
            return element.text
        except:
            return None


    # === МЕТОДЫ ПРОВЕРКИ ТЕКСТА FOOTER ===
    def scroll_to_footer(self):
        """Прокручивает страницу до футера"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        import time
        time.sleep(0.3)


    def get_copyright_text(self):
        """Получает текст Copyright"""
        try:
            copyright = self.driver.find_element(*loc.COPYRIGHT)
            return copyright.text
        except:
            return None


    def get_about_us_text(self):
        """Получает текст заголовка About us"""
        try:
            about = self.driver.find_element(*loc.ABOUT_US)
            return about.text
        except:
            return None


    def get_powered_by_text(self):
        """Получает текст ссылки Powered by"""
        try:
            powered = self.driver.find_element(*loc.POWERED_BY_ODOO)
            return powered.text
        except:
            return None
