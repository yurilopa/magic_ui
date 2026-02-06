from pages.locators.cart_locators import CartLocators as loc
from pages.base_page import BasePage


class CartPage(BasePage):
    page_url = '/shop/cart'


    def check_view_review_order_label(self):
        review_order_label = self.find(loc.REVIEW_ORDER_LABEL)
        assert review_order_label.is_displayed(), "review_order_label не найден на странице!"


    def check_view_shipping_label(self):
        shipping_label = self.find(loc.SHIPPING_LABEL)
        assert shipping_label.is_displayed(), "shipping_label не найден на странице!"


    def check_view_payment_label(self):
        payment_label = self.find(loc.PAYMENT_LABEL)
        assert payment_label.is_displayed(), "payment_label не найден на странице!"


    def check_view_title_order_overview(self):
        title_order_overview = self.find(loc.TITLE_ORDER_OVERVIEW)
        assert title_order_overview.is_displayed(), "title_order не найден на странице!"


    def check_view_empty_cart_message(self):
        empty_cart_message = self.find(loc.EMPTY_CART_MESSAGE)
        assert empty_cart_message.is_displayed(), "title_order не найден на странице!"
