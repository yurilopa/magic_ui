import pytest
from pages.all_page_text import AllPageText


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
def test_header_text_on_all_pages(driver, page_url):
    """Тест: текст всех элементов header корректен на каждой странице"""
    driver.get(f"http://testshop.qa-practice.com{page_url}")
    page = AllPageText(driver)

    errors = []  # Собираем все ошибки

    # Проверка текста Categories
    categories_text = page.get_categories_text()
    if categories_text != "Categories":
        errors.append(f"❌ Categories: ожидали 'Categories', получили '{categories_text}'")

    # Проверка текста номера телефона
    phone_text = page.get_phone_number_text()
    if phone_text != "+1 555-555-5556":
        errors.append(f"❌ Phone: ожидали '+1 555-555-5556', получили '{phone_text}'")

    # Проверка текста Sign in
    sign_in_text = page.get_sign_in_button_text()
    if sign_in_text != "Sign in":
        errors.append(f"❌ Sign in: ожидали 'Sign in', получили '{sign_in_text}'")

    # Проверка текста Contact Us
    contact_us_text = page.get_contact_us_button_text()
    if contact_us_text != "Contact Us":
        errors.append(f"❌ Contact Us: ожидали 'Contact Us', получили '{contact_us_text}'")

    # В конце проверяем, были ли ошибки
    assert not errors, f"Ошибки текста header на странице {page_url}:\n" + "\n".join(errors)


@pytest.mark.parametrize("page_url", PAGES_TO_TEST)
def test_footer_text_on_all_pages(driver, page_url):
    """Тест: текст всех элементов footer корректен на каждой странице"""
    driver.get(f"http://testshop.qa-practice.com{page_url}")
    page = AllPageText(driver)

    errors = []  # Собираем все ошибки

    # Прокручиваем до футера ОДИН РАЗ
    page.scroll_to_footer()

    # Проверка текста Copyright
    copyright_text = page.get_copyright_text()
    if copyright_text != "Copyright © Company name":
        errors.append(f"❌ Copyright: ожидали 'Copyright © Company name', получили '{copyright_text}'")

    # Проверка текста About us
    about_us_text = page.get_about_us_text()
    if about_us_text != "About us":
        errors.append(f"❌ About us: ожидали 'About us', получили '{about_us_text}'")

    # Проверка текста Powered by (проверяем, что текст НАЧИНАЕТСЯ с "Powered by")
    powered_by_text = page.get_powered_by_text()
    if not powered_by_text or not powered_by_text.startswith("Powered by"):
        errors.append(f"❌ Powered by: ожидали текст начинающийся с 'Powered by', получили '{powered_by_text}'")

    # В конце проверяем, были ли ошибки
    assert not errors, f"Ошибки текста footer на странице {page_url}:\n" + "\n".join(errors)
