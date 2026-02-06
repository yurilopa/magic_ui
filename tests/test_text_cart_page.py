# === MAIN CONTENT ===
def test_review_order_label_is(cart_page_text):
    """Тест: текста order_view"""
    cart_page_text.open_page()
    cart_page_text.check_text_review_order_label('Review Order')


def test_shipping_label_is(cart_page_text):
    """Тест: текста shipping"""
    cart_page_text.open_page()
    cart_page_text.check_text_shipping_label('Shipping')


def test_payment_label_is(cart_page_text):
    """Тест: текста payment"""
    cart_page_text.open_page()
    cart_page_text.check_text_payment_label('Payment')


def test_title_order_overview_is(cart_page_text):
    """Тест: текста order_view"""
    cart_page_text.open_page()
    cart_page_text.check_text_title_order_overview('Order overview')


def test_empty_cart_message_is(cart_page_text):
    """Тест: текста empty cart"""
    cart_page_text.open_page()
    cart_page_text.check_text_empty_cart_message('Your cart is empty!')
