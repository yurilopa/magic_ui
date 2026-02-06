from pages.locators.office_software_locators import SoftwareLocators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OfficeSoftwareVisibility(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'


    # для search_window
    def check_view_search_win(self):
        wait = WebDriverWait(self.driver, 15)
        search = wait.until(EC.visibility_of_element_located(loc.SEARCH_WIN))
        print(f"Найден элемент: {search}")
        assert search.is_displayed(), "Строка поиска не найдена на странице!"


    # для dropdown Benelux
    def check_view_benelux(self):
        dropdown_btn = self.find(loc.DROPDOWN_BTN)
        assert dropdown_btn.is_displayed(), "Кнопка c dropdown Benelux не найдена на странице!"


    # для all product
    def check_view_all_product(self):
        all_product = self.find(loc.ALL_PRODUCT)
        assert all_product.is_displayed(), "Переход на все товары не найден на странице!"


    # для multimedia
    def check_view_multimedia(self):
        multimedia = self.find(loc.MULTIMEDIA)
        assert multimedia.is_displayed(), "Переход на мультимедиа товара не найден на странице!"


    # для design_software
    def check_view_design_software(self):
        title_design_software = self.find(loc.DESIGN_SOFTWARE)
        assert title_design_software.is_displayed(), "title design software не найден на странице!"


    # для product details
    def check_view_product_details(self):
        products_details = self.find(loc.PRODUCT_DETAILS)
        assert products_details.is_displayed(), "products_attributes не найдена на странице!"


    def check_view_h1_product_details(self):
        h1_product_details = self.find(loc.H1_OFFICE_DESIGN_SOFTWARE)
        assert h1_product_details.is_displayed(), "Заголовок 'OFFICE DESIGN SOFTWARE' не найден на странице!"


    def check_view_h3_price(self):
        h3_detail_product = self.find(loc.PRODUCT_PRICE)
        assert h3_detail_product.is_displayed(), "product price не найдена на странице!"


    # для quantity
    def check_view_quantity(self):
        check_quantity = self.find(loc.QUANTITY_OPTION)
        assert check_quantity.is_displayed(), "checkbox_aluminium не найдена на странице!"


    def check_view_css_quantity(self):
        check_css_quantity = self.find(loc.CSS_QUANTITY)
        assert check_css_quantity.is_displayed(), "css_quantity не найдена на странице!"


    def check_view_minus(self):
        minus = self.find(loc.MINUS_BTN)
        assert minus.is_displayed(), "minus не найдена на странице!"


    def check_view_fa_minus(self):
        fa_minus = self.find(loc.FA_MINUS_BTN)
        assert fa_minus.is_displayed(), "fa_minus не найдена на странице!"


    def check_view_add_qty(self):
        add_qty= self.find(loc.ADD_QTY)
        assert add_qty.is_displayed(), "ADD QTY не найдена на странице!"


    def check_view_plus(self):
        plus = self.find(loc.PLUS_BTN)
        assert plus.is_displayed(), "plus не найдена на странице!"


    def check_view_fa_plus(self):
        fa_plus = self.find(loc.FA_PLUS_BTN)
        assert fa_plus.is_displayed(), "fa_plus не найдена на странице!"


    # для add to cart:
    def check_view_add_to_cart(self):
        to_cart = self.find(loc.ADD_TO_CART)
        assert to_cart.is_displayed(), "Btn add to cart не найдена на странице!"


    # для PROD_ATTRIBUTE
    def check_view_prod_attribute(self):
        attribute = self.find(loc.PROD_ATTRIBUTE)
        assert attribute.is_displayed(), "prod attribute не найдена на странице!"


    # для product terms and share
    def check_view_prod_terms(self):
        terms = self.find(loc.PROD_TERMS_AND_SHARE)
        assert terms.is_displayed(), "Terms не найдена на странице!"


    # для текста 'Terms and conditions'
    def check_view_terms_and_conditions(self):
        terms_and_conditions = self.find(loc.TERMS_AND_CONDITIONS)
        assert terms_and_conditions.is_displayed(), "Текст 'Terms and conditions' не найдена на странице!"


    # для list
    def check_view_money_back(self):
        money_back_guarantee = self.find(loc.MONEY_BACK_GUARANTEE)
        assert money_back_guarantee .is_displayed(), "Кнопка grid найдена на странице!"


    # для terms
    def check_view_link_for_terms(self):
        terms = self.find(loc.TERMS_LINK)
        assert terms.is_displayed(), "Ссылка /terms не найдена на странице!"


    # для share_link
    def check_view_share_link(self):
        share_link = self.find(loc.SHARE_LINKS)
        assert share_link.is_displayed(), "div для share links не найден на странице!"


    # для facebook link
    def check_view_facebook_link(self):
        facebook_link = self.find(loc.FACEBOOK_LINK)
        assert facebook_link.is_displayed(), "Ссылка на facebook не найдена на странице!"


    # для twitter link
    def check_view_twitter_link(self):
        twitter_link = self.find(loc.TWITTER_LINK)
        assert twitter_link.is_displayed(), "Ссылка на twitter не найдена на странице!"


    # для large meeting table
    def check_view_pinterest(self):
        pinterest = self.find(loc.PINTEREST_LINK)
        assert pinterest.is_displayed(), "Ссылка на pinterest не найдена на странице!"


    # для Combination_desk
    def check_view_email_link(self):
        email_link = self.find(loc.EMAIL_LINK)
        assert email_link.is_displayed(), "Ссылка на email не найдена не найден на странице!"
