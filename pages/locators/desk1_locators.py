from selenium.webdriver.common.by import By


class Desk1Locators:


    # === MAIN CONTENT ===
    """Локатор для title Legs"""
    LEGS_TITLE = (
        By.XPATH,
        "//b[contains(@class, 'o_products_attributes_title') and text()='Legs']"
    )

    """Локатор для Products"""
    PRODUCTS_TITLE = (By.XPATH, "//a[text()='Products']")

    """Локатор для title Desks"""
    DESKS_TITLE = (
        By.XPATH,
        "//span[contains(@class, 'd-inline-block') and text()='Desks']"
    )

    """Локатор для products_attributes"""
    PRODUCTS_ATTRIBUTE = (By.ID, 'o_products_attributes_1')

    """Локатор для steel checkbox"""
    STEEL_CHECKBOX = (
        By.XPATH,
        "//label[contains(@class, 'form-check-label') and text()='Steel']"
    )

    """Локатор для aluminium checkbox"""
    ALUMINIUM_CHECKBOX = (
        By.XPATH,
        "//label[contains(@class, 'form-check-label') and text()='Aluminium']"
    )

    """Локатор для custom checkbox"""
    CUSTOM_CHECKBOX = (
        By.XPATH,
        "//label[contains(@class, 'form-check-label') and text()='Custom']"
    )

    """Локатор для Price Range"""
    PRICE_RANGE = (By.XPATH, "//b[text()='Price Range']")

    """Локатор для multirange-min"""
    PRICE_RANGE_SECTION = (By.ID, "o_wsale_price_range_option")
    MULTIRANGE_WRAPPER = (By.CSS_SELECTOR, ".multirange-wrapper")
    MULTIRANGE_MIN = (By.CSS_SELECTOR, "span.multirange-min")
    MULTIRANGE_MAX = (By.CSS_SELECTOR, "span.multirange-max")

    """Локатор для multiple на странице"""
    PRICE_RANGE_SLIDER = (By.CSS_SELECTOR, ".multirange-wrapper")

    """Локатор для поиска строки поиска"""
    SEARCH_WIN = (By.CSS_SELECTOR,
                  'input[type="search"]:not(.rounded-start-pill)')

    """Локатор для поиска SEARCH_BTN на странице"""
    SEARCH_BTN = (By.CSS_SELECTOR,
                  'button[type="submit"].oe_search_button.btn.btn-light')

    """Локатор для поиска левого (с Бенилюкс) Dropdown_BTN на странице"""
    DROPDOWN_BTN = (By.XPATH,
                    "//a[@role='button' and normalize-space()='Benelux']")

    """Локатор для title Sort By:"""
    SORT_BY = (
        By.XPATH,
        "//small[contains(@class, 'text-muted') and text()='Sort By:']"
    )

    """Локатор для Featured"""
    FEATURED_DROPDOWN = (By.XPATH, '//span[text()="Featured"]')

    """Локатор для поиска grid btn"""
    GRID = (By.CSS_SELECTOR,
            'input[name="wsale_products_layout"][value="grid"]')

    """Локатор для поиска list btn"""
    LIST = (By.CSS_SELECTOR,
            'input[name="wsale_products_layout"][value="list"]')

    """Локатор для Components"""
    COMPONENTS = (By.XPATH, '//span[text()="Components"]')

    """Локатор для CUSTOMIZABLE DESK"""
    CUSTOMIZABLE_DESK = (By.CSS_SELECTOR,
                         'a[href="/shop/customizable-desk-9?category=1"]')

    """Локатор для CORNER DESK LEFT SID"""
    CORNER_DESK_LEFT_SID = (
        By.CSS_SELECTOR,
        'a[href="/shop/furn-1118-corner-desk-left-sit-18?category=1"]'
    )

    """Локатор для acoustic block"""
    ACOUSTIC_BLOCK_SCREENS = (
        By.CSS_SELECTOR,
        'a[href="/shop/furn-6666-acoustic-bloc-screens-23?category=1"]'
    )

    """Локатор для desk 4 person"""
    FOUR_PERSON_DESK = (By.CSS_SELECTOR,
                        'a[href="/shop/furn-8220-four-person-desk-25?category=1"]')

    """Локатор для large table"""
    LARGE_TABLE = (By.CSS_SELECTOR,
                   'a[href="/shop/furn-6741-large-meeting-table-26?category=1"]')

    """Локатор для desk combination"""
    COMBINATION_DESK = (By.CSS_SELECTOR,
                        'a[href="/shop/furn-7800-desk-combination-8?category=1"]')

    """Локатор для CORNER DESK RIGHT SID"""
    CORNER_DESK_RIGHT_SID = (By.CSS_SELECTOR,
                             'a[href="/shop/e-com06-corner-desk-right-sit-10?category=1"]')

    """Локатор для large desk"""
    LARGE_DESK = (By.CSS_SELECTOR,
                  'a[href="/shop/e-com09-large-desk-13?category=1"]')

    """Локатор для desk stand"""
    STAND_WITH_SCREEN_DESK = (
        By.CSS_SELECTOR,
        'a[href="/shop/furn-7888-desk-stand-with-screen-21?category=1"]'
    )
