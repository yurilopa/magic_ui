from selenium.webdriver.common.by import By


class CartLocators:  # ← КЛАСС, не переменная!
    """Локаторы для страницы cart"""

    # === ЛОКАТОРЫ HEADER ===
    """Локатор для поиска logo"""
    LOGO = (By.CLASS_NAME, 'mb-4')

    """Локатор для поиска кнопки categories"""
    CATEGORIES = (By.LINK_TEXT, 'Categories')

    """Локатор для поиска cart icon"""
    CART_ICON = (By.CSS_SELECTOR, 'a[href="/shop/cart"]')

    """Локатор для поиска иконки поиска"""
    SEARCH_ICON = (By.CSS_SELECTOR, "a[title='Search']")

    """Локатор для поиска телефона"""
    PHONE_NUMBER = (By.LINK_TEXT, "+1 555-555-5556")

    """Локатор для поиска кнопки sig in"""
    SIGN_IN_BTN = (By.LINK_TEXT, 'Sign in')

    """Локатор для поиска кнопки Contact Us"""
    CONTACT_US_BUTTON = (By.LINK_TEXT, "Contact Us")

    # === ЛОКАТОРЫ MAIN CONTENT ===
    """Локатор для поиска REVIEW_ORDER_LABEL"""
    REVIEW_ORDER_LABEL = (By.XPATH, "//p[normalize-space()='Review Order']")

    """Локатор для поиска Shipping"""
    SHIPPING_LABEL = (By.XPATH, "//p[normalize-space()='Shipping']")

    """Локатор для поиска Payment"""
    PAYMENT_LABEL = (By.XPATH, "//p[normalize-space()='Payment']")

    """Локатор для поиска ORDER_OVERVIEW"""
    TITLE_ORDER_OVERVIEW = (By.CLASS_NAME, 'mb-4')

    """Локатор для поиска сообщения о пустой корзине"""
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your cart is empty!')]")

    # === ЛОКАТОРЫ FOOTER ===
    """Локатор для поиска About us на странице"""
    FOOTER_TITLE = (By.XPATH, "//h5[text()='About us']")

    """Локатор для поиска copyright на странице"""
    COPYRIGHT = (By.XPATH, "//h5[text()='About us']")
