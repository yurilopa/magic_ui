from pages.locators.cart_locators import CartLocators as loc
from pages.base_page import BasePage


class CartPageText(BasePage):
    page_url = '/shop/cart'


    def check_text_review_order_label(self, expected_text):
        review_order_label = self.find(loc.REVIEW_ORDER_LABEL)
        actual_text = review_order_label.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_shipping_label(self, expected_text):
        shipping_label = self.find(loc.SHIPPING_LABEL)
        actual_text = shipping_label.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_payment_label(self, expected_text):
        payment_label = self.find(loc.PAYMENT_LABEL)
        actual_text = payment_label.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_title_order_overview(self, expected_text):
        title_order_overview = self.find(loc.TITLE_ORDER_OVERVIEW)
        actual_text = title_order_overview.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_empty_cart_message(self, expected_text):
        empty_cart_message = self.find(loc.EMPTY_CART_MESSAGE)
        actual_text = empty_cart_message.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"
