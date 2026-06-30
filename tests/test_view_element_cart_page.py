# === MAIN CONTENT ===
def test_review_order_label_is_visible(cart_page):
    """Тест: заголовок order_view виден"""
    cart_page.open_page()
    cart_page.check_view_review_order_label()


def test_shipping_label_is_visible(cart_page):
    """Тест: заголовок shipping виден"""
    cart_page.open_page()
    cart_page.check_view_shipping_label()


def test_payment_label_is_visible(cart_page):
    """Тест: заголовок payment виден"""
    cart_page.open_page()
    cart_page.check_view_payment_label()


def test_title_order_overview_is_visible(cart_page):
    """Тест: заголовок order_view виден"""
    cart_page.open_page()
    cart_page.check_view_title_order_overview()


def test_empty_cart_message_is_visible(cart_page):
    """Тест: заголовок order_view виден"""
    cart_page.open_page()
    cart_page.check_view_empty_cart_message()
