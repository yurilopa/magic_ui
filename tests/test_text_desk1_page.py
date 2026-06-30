# === MAIN CONTENT ===
def test_text_title_legs(desk1_page_text):
    """Тест: текст заголовка Legs"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_legs_header_title_is('Legs')


def test_text_title_product(desk1_page_text):
    """Тест: текст заголовка Products"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_products_is('Products')


def test_text_title_desks(desk1_page_text):
    """Тест: текст заголовка Desks"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_desks_is('Desks')


def test_text_steel_checkbox_is(desk1_page_text):
    """Тест: текст чекбокса Steel"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_steel_checkbox_is('Steel')


def test_text_aluminium_checkbox_is(desk1_page_text):
    """Тест: текст чекбокса Aluminium"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_aluminium_checkbox_is('Aluminium')


def test_text_custom_checkbox_is(desk1_page_text):
    """Тест: текст чекбокса Custom"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_custom_checkbox_is('Custom')


def test_text_price_range_is(desk1_page_text):
    """Тест: текст заголовка Price Range"""
    desk1_page_text.open_page()
    desk1_page_text.check_text_price_range_is('Price Range')


def test_text_multirange_min_is(desk1_page_text):
    """Тест: текст заголовка Multi Range min"""
    desk1_page_text.open_page()
    desk1_page_text.check_multirange_min_text('$ 85.00')


def test_text_multirange_max_is(desk1_page_text):
    """Тест: текст заголовка Multi Range max"""
    desk1_page_text.open_page()
    desk1_page_text.check_multirange_max_text('$ 4,000.00')


def test_text_dropdown_is(desk1_page_text):
    """Тест: текст Benelux"""
    desk1_page_text.open_page()
    desk1_page_text.check_dropdown_is('Benelux')


def test_text_sort_by_is(desk1_page_text):
    """Тест: текста sort_by """
    desk1_page_text.open_page()
    desk1_page_text.check_sort_by_is('Sort By:')


def test_text_dropdown_featured_is(desk1_page_text):
    """Тест: текста в dropdown featured """
    desk1_page_text.open_page()
    desk1_page_text.check_dropdown_featured_is('Featured')


def test_text_components_btn_is(desk1_page_text):
    """Тест: текста sort_by """
    desk1_page_text.open_page()
    desk1_page_text.check_components_btn_is('Components')

