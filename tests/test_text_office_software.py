# === MAIN CONTENT ===
def test_text_benelux_is(office_software_text):
    """Тест: текст place holdera search window Error AssertionError: Ожидали 'Search...', получили '' """
    office_software_text.open_page()
    office_software_text.check_benelux_is('Benelux')


def test_text_title_design_software_is(office_software_text):
    """Тест: текст заголовка Legs"""
    office_software_text.open_page()
    office_software_text.check_text_title_design_software_is('Office Design Software')


def test_text_h1_product_details_is(office_software_text):
    """Тест: текст заголовка Product details"""
    office_software_text.open_page()
    office_software_text.check_text_h1_product_details_is('Office Design Software')


def test_text_h3_product_price_is(office_software_text):
    """Тест: текст заголовка Product price"""
    office_software_text.open_page()
    office_software_text.check_text_h3_product_price_is('$ 280.00')


def test_text_terms_and_conditions_is(office_software_text):
    """Тест: текст чекбокса Aluminium"""
    office_software_text.open_page()
    office_software_text.check_text_terms_and_conditions_is('Terms and Conditions')


def test_text_money_back_is(office_software_text):
    """Тест: текст чекбокса Custom"""
    office_software_text.open_page()
    office_software_text.check_text_money_back_is('30-day money-back guarantee')


def test_text_shipping_is(office_software_text):
    """Тест: текст чекбокса Custom"""
    office_software_text.open_page()
    office_software_text.check_text_money_back_is('Shipping: 2-3 Business Days')
