from selenium.webdriver.common.by import By


class AllPageLocators:


    # === ЛОКАТОРЫ HEADER with text===
    """Локатор для поиска кнопки categories"""
    CATEGORIES = (By.LINK_TEXT, 'Categories')

    """Локатор для поиска телефона"""
    PHONE_NUMBER = (By.LINK_TEXT, "+1 555-555-5556")

    """Локатор для поиска кнопки Contact Us"""
    CONTACT_US_BUTTON = (By.LINK_TEXT, "Contact Us")


    # === ЛОКАТОРЫ HEADER ===
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand img")
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign in")
    CART_ICON = (By.CSS_SELECTOR, "a[href='/shop/cart']")
    SEARCH_ICON = (By.CSS_SELECTOR, "a[title='Search']")

    # === ЛОКАТОРЫ FOOTER ===
    COPYRIGHT = (By.XPATH, "//*[contains(text(), 'Copyright')]")
    ABOUT_US = (By.XPATH, "//h5[text()='About us']")
    POWERED_BY_ODOO = (By.XPATH, "//*[contains(text(), 'Powered by')]")
