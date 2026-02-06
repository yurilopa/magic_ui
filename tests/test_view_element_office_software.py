# === MAIN CONTENT ===
def test_search_view(office_software_visibility):
    """Тест: кнопка search видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_search_button()


def test_benelux_view(office_software_visibility):
    """Тест: кнопка dropdown benelux видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_benelux()


def test_all_product_view(office_software_visibility):
    """Тест: кнопка-ссылка для перехода на все товары видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_all_product()


def test_multimedia_view(office_software_visibility):
    """Тест: кнопка-ссылка для перехода на все товары видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_multimedia()


def test_title_design_software_view(office_software_visibility):
    """Тест: заголовок software виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_design_software()


def test_product_details_view(office_software_visibility):
    """Тест: блок Product details виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_products_details()


def test_h1_product_details_view(office_software_visibility):
    """Тест: заголовок Product details виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_h1_product_details()


def test_h3_product_price_view(office_software_visibility):
    """Тест: заголовок Product price виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_h3_price()


def test_quantity_view(office_software_visibility):
    """Тест: счетчик quantity виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_quantity()


def test_css_quantity_view(office_software_visibility):
    """Тест: счетчик quantity виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_css_quantity()


def test_minus_view(office_software_visibility):
    """Тест: minus виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_minus()


def test_fa_minus_view(office_software_visibility):
    """Тест: fa_minus виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_fa_minus()


def test_add_qty_view(office_software_visibility):
    """Тест: 1 в qty виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_add_qty()


def test_plus_view(office_software_visibility):
    """Тест: plus виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_plus()


def test_fa_plus_view(office_software_visibility):
    """Тест: fa_plus виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_fa_plus()


def test_add_to_cart_view(office_software_visibility):
    """Тест: multirange_min виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_add_to_cart()


def test_prod_attribute_view(office_software_visibility):
    """Тест: multirange_max виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_prod_attribute()


def test_prod_terms_view(office_software_visibility):
    """Тест: multiple виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_prod_terms()


def test_terms_and_conditions_view(office_software_visibility):
    """Тест: окно search видна"""
    office_software_visibility.open_page()
    office_software_visibility.driver.maximize_window()
    office_software_visibility.check_view_terms_and_conditions()


def test_money_back_guarantee_view(office_software_visibility):
    """Тест: текст money back guarantee виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_money_back()


def test_shipping_view(office_software_visibility):
    """Тест: кнопка dropdown benelux видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_money_back()


def test_link_for_terms_view(office_software_visibility):
    """Тест: terms виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_link_for_terms()


def test_link_share_view(office_software_visibility):
    """Тест: id share виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_share_link()


def test_facebook_link_view(office_software_visibility):
    """Тест: ссылка facebook видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_facebook_link()


def test_twitter_link_view(office_software_visibility):
    """Тест: ссылка twitter видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_twitter_link()


def test_pinterest_view(office_software_visibility):
    """Тест: ссылка pinterest видна"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_pinterest()


def test_email_link_view(office_software_visibility):
    """Тест: товар four person desk виден"""
    office_software_visibility.open_page()
    office_software_visibility.check_view_email_link()
