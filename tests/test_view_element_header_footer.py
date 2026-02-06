import pytest
from pages.all_page import HeaderPage


# Список страниц
PAGES_TO_TEST = [
    "/",
    "/shop",
    "/shop/cart",
    "/shop/checkout",
    "/shop/category/desks-8",
    "/web/login",
    "/contactus",
]


@pytest.mark.parametrize("page_url", PAGES_TO_TEST)
def test_header_elements_visible_on_all_pages(driver, page_url):
    """Тест: все элементы header видны на каждой странице"""
    driver.get(f"http://testshop.qa-practice.com{page_url}")
    page = HeaderPage(driver)

    errors = []  # Собираем все ошибки

    if not page.is_logo_visible():
        errors.append(f"❌ Логотип не найден")

    if not page.is_sign_in_button_visible():
        errors.append(f"❌ Кнопка Sign In не найдена")

    if not page.is_cart_icon_visible():
        errors.append(f"❌ Иконка корзины не найдена")

    if not page.is_search_icon_visible():
        errors.append(f"❌ Иконка поиска не найдена")

    # В конце проверяем, были ли ошибки
    assert not errors, f"Ошибки на странице {page_url}:\n" + "\n".join(errors)


@pytest.mark.parametrize("page_url", PAGES_TO_TEST)
def test_footer_elements_visible_on_all_pages(driver, page_url):
    """Тест: все элементы footer видны на каждой странице"""
    driver.get(f"http://testshop.qa-practice.com{page_url}")
    page = HeaderPage(driver)

    errors = []  # Собираем все ошибки
    # Прокручиваем до футера ОДИН РАЗ
    page.scroll_to_footer()

    if not page.is_copyright_visible():
        errors.append(f"❌ Copyright не найден")

    if not page.is_about_us_visible():
        errors.append(f"❌ 'About us' не найдено")

    if not page.is_powered_by_odoo_visible():
        errors.append(f"❌ 'Powered by Odoo' не найдено")

    # В конце проверяем, были ли ошибки
    assert not errors, f"Ошибки на странице {page_url}:\n" + "\n".join(errors)
