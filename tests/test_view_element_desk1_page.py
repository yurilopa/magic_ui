# === MAIN CONTENT ===
def test_title_legs_view(desk1_page_visibility):
    """Тест: заголовок Legs виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_legs_header_title_view()


def test_title_product_view(desk1_page_visibility):
    """Тест: заголовок Products виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_products_view()


def test_title_desks_view(desk1_page_visibility):
    """Тест: заголовок Desks виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_desks_view()


def test_products_attributes_view(desk1_page_visibility):
    """Тест: блок Products Attributes виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_products_attributes_view()


def test_checkbox_steel_view(desk1_page_visibility):
    """Тест: чекбокс Steel виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_checkbox_steel_view()


def test_checkbox_aluminium_view(desk1_page_visibility):
    """Тест: чекбокс Aluminium виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_checkbox_aluminium_view()


def test_checkbox_custom_view(desk1_page_visibility):
    """Тест: чекбокс Custom виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_checkbox_custom_view()


def test_price_range_view(desk1_page_visibility):
    """Тест: заголовок Price Range виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_price_range_view()


def test_multirange_min_view(desk1_page_visibility):
    """Тест: multirange_min виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_multirange_min_view()


def test_multirange_max_view(desk1_page_visibility):
    """Тест: multirange_max виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_multirange_max_view()


def test_multiple_view(desk1_page_visibility):
    """Тест: multiple виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_multiple_view_with_scroll()


def test_search_win_view(desk1_page_visibility):
    """Тест: окно search видна"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.driver.maximize_window()
    desk1_page_visibility.check_view_search_win()


def test_search_view(desk1_page_visibility):
    """Тест: кнопка search видна"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_search_button()


def test_benelux_view(desk1_page_visibility):
    """Тест: кнопка dropdown benelux видна"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_dropdown_benelux()


def test_sort_by_view(desk1_page_visibility):
    """Тест: кнопка Sort By виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_sort_by()


def test_featured_view(desk1_page_visibility):
    """Тест: кнопка dropdown benelux видна"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_dropdown_featured()


def test_grid_view(desk1_page_visibility):
    """Тест: окно search видна"""
    desk1_page_visibility.open_page()
    #desk1_page_visibility.driver.maximize_window()
    desk1_page_visibility.check_view_grid()


def test_list_view(desk1_page_visibility):
    """Тест: окно search видна"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.driver.maximize_window()
    desk1_page_visibility.check_view_list()


def test_components_view(desk1_page_visibility):
    """Тест: кнопка components видна"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_components()


def test_customizable_desk_view(desk1_page_visibility):
    """Тест: товар customizable desk виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_customizable_desk()


def test_corner_desk_view(desk1_page_visibility):
    """Тест: товар corner desk виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_corner_desk_left_sid()


def test_acoustic_bloc_screen_view(desk1_page_visibility):
    """Тест: товар acoustic bloc screen виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_acoustic_bloc_screen()


def test_four_person_desk_view(desk1_page_visibility):
    """Тест: товар four person desk виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_four_person_desk()


def test_large_meeting_table(desk1_page_visibility):
    """Тест: товар large_meeting_table виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_large_meeting_table()


def test_combination_desk(desk1_page_visibility):
    """Тест: товар combination desk виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_combination_desk()


def test_corner_desk_right_sid(desk1_page_visibility):
    """Тест: товар corner desk right sid виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_corner_desk_right_sid()


def test_large_desk_view(desk1_page_visibility):
    """Тест: товар large desk виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_large_desk()


def test_stad_with_screen_view(desk1_page_visibility):
    """Тест: товар stad with screen виден"""
    desk1_page_visibility.open_page()
    desk1_page_visibility.check_view_desk_stad_with_screen()
