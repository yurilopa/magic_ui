from selenium.webdriver.common.by import By


class SoftwareLocators:


    # === MAIN CONTENT ===
    """Локатор для поиска строки поиска"""
    SEARCH_WIN = (By.CSS_SELECTOR, 'input[type="search"]:not(.rounded-start-pill)')

    """Локатор для поиска Dropdown Бенилюкс на странице"""
    DROPDOWN_BTN = (By.XPATH, "//a[@role='button' and text()='Benelux']")

    """Локатор для поиска ALL PRODUCT"""
    ALL_PRODUCT = (By.CSS_SELECTOR, 'a[href="/shop"]')

    """Локатор для поиска MULTIMEDIA"""
    MULTIMEDIA = (By.CSS_SELECTOR, 'a[href="/shop/category/multimedia-9"]')

    """Локатор для поиска title Office Design Software"""
    DESIGN_SOFTWARE = (By.XPATH, '//span[text()="Office Design Software"]')

    """Локатор для поиска products_details"""
    PRODUCT_DETAILS = (By.ID, 'product_details')

    """Локатор для поиска заголовка Office Design Software на странице"""
    H1_OFFICE_DESIGN_SOFTWARE = (By.XPATH,
                                 "//h1[@itemprop='name' and text()='Office Design Software']")

    """Локатор для поиска price на странице"""
    PRODUCT_PRICE = (By.XPATH, "//h3[@class='css_editable_mode_hidden']")

    """Локатор для quantity"""
    QUANTITY_OPTION = (By.ID, "o_wsale_cta_wrapper")

    """Локатор для css quantity"""
    CSS_QUANTITY = (By.CSS_SELECTOR, ".css_quantity")

    """Локатор для поиска кнопки "-" на странице"""
    MINUS_BTN = (By.XPATH, "//a[@title='Remove one']")

    """Локатор для поиска FA MINUS на странице"""
    FA_MINUS_BTN = (By.CLASS_NAME, 'fa-minus')

    """Локатор для поиска "1" на стр"""
    ADD_QTY = (By.CSS_SELECTOR, 'input[type="text"].form-control.quantity.text-center')

    """Локатор для поиска кнопки "+" на странице"""
    PLUS_BTN = (By.XPATH, "//a[@title='Add one']")

    """Локатор для поиска FA PLUS на странице"""
    FA_PLUS_BTN = (By.CLASS_NAME, 'fa-plus')

    """Локатор для поиска add to cart"""
    ADD_TO_CART = (By.ID, 'add_to_cart')

    """Локатор для поиска product attribute simple"""
    PROD_ATTRIBUTE = (By.ID, 'product_attributes_simple')

    """Локатор для поиска product terms and share"""
    PROD_TERMS_AND_SHARE = (By.ID, 'o_product_terms_and_share')

    """Локатор для Terms and Conditions"""
    TERMS_AND_CONDITIONS = (By.XPATH, "//u[text()='Terms and Conditions']")

    """Локатор для MONEY BACK GUARANTEE"""
    MONEY_BACK_GUARANTEE = (By.XPATH,
                            "//div[@id='o_product_terms_and_share']//p[@class='text-muted mb-0']")

    """Локатор для LINK /TERMS"""
    TERMS_LINK = (By.CSS_SELECTOR, 'a[href="/terms"]')

    """Локатор для links share"""
    SHARE_LINKS = (By.XPATH, "//div[@data-snippet='s_share']")

    """Локатор для facebook link"""
    FACEBOOK_LINK = (By.CSS_SELECTOR, "a[aria-label='Facebook']")

    """Локатор для twitter link"""
    TWITTER_LINK = (By.CSS_SELECTOR, "a[aria-label='Twitter']")

    """Локатор для pinterest link"""
    PINTEREST_LINK = (By.CSS_SELECTOR, "a[aria-label='Pinterest']")

    """Локатор для emil"""
    EMAIL_LINK = (By.CSS_SELECTOR, "a[aria-label='Email']")

    """Локатор для CORNER DESK RIGHT SID"""
    CORNER_DESK_RIGHT_SID = (By.CSS_SELECTOR,
                             'a[href="/shop/e-com06-corner-desk-right-sit-10?category=1"]')

    """Локатор для large desk"""
    LARGE_DESK = (By.CSS_SELECTOR,
                  'a[href="/shop/e-com09-large-desk-13?category=1"]')

    """Локатор для desk stand"""
    STAND_WITH_SCREEN_DESK = (By.CSS_SELECTOR,
                              'a[href="/shop/furn-7888-desk-stand-with-screen-21?category=1"]')

    """Локатор для поиска SEARCH_BTN на странице"""
    SEARCH_BTN = (By.CSS_SELECTOR,
                  'button[type="submit"].oe_search_button.btn.btn-light')


    """Локатор для title Sort By:"""
    SORT_BY = (
        By.XPATH, "//small[contains(@class, 'text-muted') and text()='Sort By:']"
    )

    """Локатор для Featured"""
    FEATURED_DROPDOWN = (
        By.XPATH, "//span[contains(@class, 'dropdown-toggle') and text()='Featured']"
    )

    """Локатор для поиска grid btn"""
    GRID = (By.CSS_SELECTOR, 'input[name="wsale_products_layout"][value="grid"]')

    """Локатор для поиска list btn"""
    LIST = (By.CSS_SELECTOR, 'input[name="wsale_products_layout"][value="list"]')

    """Локатор для Featured"""
    COMPONENTS = (By.XPATH, '//span[text()="Components"]')
