from pages.locators.desk1_locators import Desk1Locators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Desk1PageText(BasePage):
    page_url = '/shop/category/desks-1'


    # === MAIN CONTENT ===
    def check_text_legs_header_title_is(self, expected_text):
        header_title = self.find(loc.LEGS_TITLE)
        actual_text = header_title.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_products_is(self, expected_text):
        title_products = self.find(loc.PRODUCTS_TITLE)
        actual_text = title_products.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_desks_is(self, expected_text):
        title_desks = self.find(loc.DESKS_TITLE)
        actual_text = title_desks.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_steel_checkbox_is(self, expected_text):
        checkbox_steel = self.find(loc.STEEL_CHECKBOX)
        actual_text = checkbox_steel.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_aluminium_checkbox_is(self, expected_text):
        checkbox_aluminium = self.find(loc.ALUMINIUM_CHECKBOX)
        actual_text = checkbox_aluminium.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_custom_checkbox_is(self, expected_text):
        checkbox_custom = self.find(loc.CUSTOM_CHECKBOX)
        actual_text = checkbox_custom.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_price_range_is(self, expected_text):
        price_range = self.find(loc.PRICE_RANGE)
        actual_text = price_range.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_multirange_min_text(self, expected_text):
        """Проверка текста в элементе multirange-min
        Args:
            expected_text: Ожидаемый текст (по умолчанию "$ 85.00")
        """
        # Ждем загрузки wrapper
        wait = WebDriverWait(self.driver, 10)
        wrapper = wait.until(
            EC.presence_of_element_located(loc.MULTIRANGE_WRAPPER)
        )
        # Скроллим к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", wrapper)
        # Находим элемент и получаем текст
        multirange_min = wait.until(
            EC.visibility_of_element_located(loc.MULTIRANGE_MIN)
        )
        actual_text = multirange_min.text
        # Проверяем
        assert actual_text == expected_text, \
            f"Текст multirange-min не совпадает! Ожидалось: '{expected_text}', Получено: '{actual_text}'"


    def check_multirange_max_text(self, expected_text):
        """Проверка текста в элементе multirange-max
        Args:
            expected_text: Ожидаемый текст (по умолчанию "$ 4,000.00")
        """
        # Ждем загрузки wrapper
        wait = WebDriverWait(self.driver, 10)
        wrapper = wait.until(
            EC.presence_of_element_located(loc.MULTIRANGE_WRAPPER)
        )
        # Скроллим к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", wrapper)
        # Находим элемент и получаем текст
        multirange_max = wait.until(
            EC.visibility_of_element_located(loc.MULTIRANGE_MAX)
        )
        actual_text = multirange_max.text
        # Проверяем
        assert actual_text == expected_text, \
            f"Текст multirange-min не совпадает! Ожидалось: '{expected_text}', Получено: '{actual_text}'"


    def check_dropdown_is(self, expected_text):
        dropdown_is = self.find(loc.DROPDOWN_BTN)
        dropdown_benelux = dropdown_is.text
        assert dropdown_benelux == expected_text, \
            f"Ожидали '{expected_text}', получили '{dropdown_benelux}'"


    def check_sort_by_is(self, expected_text):
        sort_by_is = self.find(loc.SORT_BY)
        sort_by = sort_by_is.text
        assert sort_by == expected_text, \
            f"Ожидали '{expected_text}', получили '{sort_by}'"


    def check_dropdown_featured_is(self, expected_text):
        featured_is = self.find(loc.FEATURED_DROPDOWN)
        featured = featured_is.text
        assert featured == expected_text, \
            f"Ожидали '{expected_text}', получили '{featured}'"


    def check_components_btn_is(self, expected_text):
        components_btn_is = self.find(loc.COMPONENTS)
        components_btn = components_btn_is.text
        assert components_btn == expected_text, \
            f"Ожидали '{expected_text}', получили '{components_btn}'"
