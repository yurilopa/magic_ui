from selenium.webdriver.common.by import By


class CartLocators:
    """Локаторы для страницы cart"""


    # === ЛОКАТОРЫ MAIN CONTENT ===
    """Локатор для поиска REVIEW_ORDER_LABEL"""
    REVIEW_ORDER_LABEL = (By.XPATH, "//p[text()='Review Order']")

    """Локатор для поиска Shipping"""
    SHIPPING_LABEL = (By.XPATH, "//p[text()='Shipping']")

    """Локатор для поиска Payment"""
    PAYMENT_LABEL = (By.XPATH, "//p[text()='Payment']")

    """Локатор для поиска ORDER_OVERVIEW"""
    TITLE_ORDER_OVERVIEW = (By.CLASS_NAME, 'mb-4')

    """Локатор для поиска сообщения о пустой корзине"""
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your cart is empty!')]")
