from pages.locators.desk1_locators import Desk1Locators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Desk1PageVisibility(BasePage):
    page_url = '/shop/category/desks-1'


    # === MAIN CONTENT ===
    def check_legs_header_title_view(self):
        header_title = self.find(loc.LEGS_TITLE)
        assert header_title.is_displayed(), "'legs' не найден на странице!"


    def check_products_view(self):
        title_products = self.find(loc.PRODUCTS_TITLE)
        assert title_products.is_displayed(), "products не найдена на странице!"


    def check_desks_view(self):
        title_desks = self.find(loc.DESKS_TITLE)
        assert title_desks.is_displayed(), "desks не найдена на странице!"


    def check_products_attributes_view(self):
        products_attributes = self.find(loc.PRODUCTS_ATTRIBUTE)
        assert products_attributes.is_displayed(), "products_attributes не найдена на странице!"


    def check_checkbox_steel_view(self):
        checkbox_steel = self.find(loc.STEEL_CHECKBOX)
        assert checkbox_steel.is_displayed(), "checkbox_steel не найдена на странице!"


    def check_checkbox_aluminium_view(self):
        checkbox_aluminium = self.find(loc.ALUMINIUM_CHECKBOX)
        assert checkbox_aluminium.is_displayed(), "checkbox_aluminium не найдена на странице!"


    def check_checkbox_custom_view(self):
        checkbox_custom = self.find(loc.CUSTOM_CHECKBOX)
        assert checkbox_custom.is_displayed(), "checkbox_custom не найдена на странице!"


    def check_price_range_view(self):
        price_range = self.find(loc.PRICE_RANGE)
        assert price_range.is_displayed(), "Price Range не найдена на странице!"


    # для multirange_min
    def check_multirange_min_view(self):
        # Ждем загрузки wrapper
        wait = WebDriverWait(self.driver, 10)
        wrapper = wait.until(
            EC.presence_of_element_located(loc.MULTIRANGE_WRAPPER)
        )
        # Скроллим к нему
        self.driver.execute_script("arguments[0].scrollIntoView(true);", wrapper)
        # Ждем появления span
        multirange_min = wait.until(
            EC.visibility_of_element_located(loc.MULTIRANGE_MIN)
        )
        print(f"Найден элемент: {multirange_min.text}")  # Для отладки
        assert multirange_min.is_displayed(), "multirange-min не отображается!"


    # для multirange_max
    def check_multirange_max_view(self):
        # Ждем загрузки wrapper
        wait = WebDriverWait(self.driver, 10)
        wrapper = wait.until(
            EC.presence_of_element_located(loc.MULTIRANGE_WRAPPER)
        )
        # Скроллим к нему
        self.driver.execute_script("arguments[0].scrollIntoView(true);", wrapper)
        # Ждем появления span
        multirange_max = wait.until(
            EC.visibility_of_element_located(loc.MULTIRANGE_MAX)
        )
        print(f"Найден элемент: {multirange_max.text}")  # Для отладки
        assert multirange_max.is_displayed(), "multirange-max не отображается!"


    # для multiple
    def check_multiple_view_with_scroll(self):
        # Ждем загрузки wrapper
        wait = WebDriverWait(self.driver, 10)
        wrapper = wait.until(
            EC.presence_of_element_located(loc.MULTIRANGE_WRAPPER)
        )
        # Скроллим к нему
        self.driver.execute_script("arguments[0].scrollIntoView(true);", wrapper)
        # Ждем появления span
        multiple = wait.until(
            EC.visibility_of_element_located(loc.PRICE_RANGE_SLIDER)
        )
        # print(f"Найден элемент: {multiple}")  # Для отладки
        assert multiple.is_displayed(), "multirange-max не отображается!"


    # для search_window
    def check_view_search_win(self):
        wait = WebDriverWait(self.driver, 15)
        search = wait.until(EC.visibility_of_element_located(loc.SEARCH_WIN))
        # print(f"Найден элемент: {search}") # Для отладки
        assert search.is_displayed(), "Строка поиска не найдена на странице!"


    # для search_btn
    def check_view_search_button(self):
        search_btn = self.find(loc.SEARCH_BTN)
        assert search_btn.is_displayed(), "Кнопка Search не найдена на странице!"


    # для dropdown Benelux
    def check_view_dropdown_benelux(self):
        dropdown_btn = self.find(loc.DROPDOWN_BTN)
        assert dropdown_btn.is_displayed(), "Кнопка c dropdown Benelux не найдена на странице!"


    # для Sort_By:
    def check_view_sort_by(self):
        title_desks = self.find(loc.SORT_BY)
        assert title_desks.is_displayed(), "Sort_By не найдена на странице!"


    # для FEATURED_DROPDOWN
    def check_view_dropdown_featured(self):
        featured_btn = self.find(loc.FEATURED_DROPDOWN)
        assert featured_btn.is_displayed(), "Кнопка c dropdown Featured не найдена на странице!"


    # для grid
    def check_view_grid(self):
        wait = WebDriverWait(self.driver, 15)
        grid = wait.until(EC.visibility_of_element_located(loc.GRID))
        # print(f"Найден элемент: {grid}") # Для отладки
        assert grid.is_displayed(), "Кнопка grid найдена на странице!"


    # для list
    def check_view_list(self):
        wait = WebDriverWait(self.driver, 15)
        grid = wait.until(EC.visibility_of_element_located(loc.LIST))
        # print(f"Найден элемент: {grid}") # Для отладки
        assert grid.is_displayed(), "Кнопка grid найдена на странице!"


    # для Components
    def check_view_components(self):
        components = self.find(loc.COMPONENTS)
        assert components.is_displayed(), "Кнопка components не найдена на странице!"


    # для Customizable desk
    def check_view_customizable_desk(self):
        customizable_desk = self.find(loc.CUSTOMIZABLE_DESK)
        assert customizable_desk.is_displayed(), "Товар customizable desk не найден на странице!"


    # для Corner desk left sid
    def check_view_corner_desk_left_sid(self):
        corner_desk_left_sid = self.find(loc.CORNER_DESK_LEFT_SID)
        assert corner_desk_left_sid.is_displayed(), "Товар corner desk left sid не найден на странице!"


    # для Acoustic bloc screen
    def check_view_acoustic_bloc_screen(self):
        acoustic_bloc_screen = self.find(loc.ACOUSTIC_BLOCK_SCREENS)
        assert acoustic_bloc_screen.is_displayed(), "Товар acoustic bloc screen btn не найден на странице!"


    # для four person desk
    def check_view_four_person_desk(self):
        four_person_desk = self.find(loc.FOUR_PERSON_DESK)
        assert four_person_desk.is_displayed(), "Товар four person desk не найден на странице!"


    # для large meeting table
    def check_view_large_meeting_table(self):
        large_meeting_table = self.find(loc.LARGE_TABLE)
        assert large_meeting_table.is_displayed(), "Товар large meeting table не найден на странице!"


    # для Combination_desk
    def check_view_combination_desk(self):
        combination_desk = self.find(loc.COMBINATION_DESK)
        assert combination_desk.is_displayed(), "Товар combination desk не найден на странице!"


    # для Corner desk right sid
    def check_view_corner_desk_right_sid(self):
        corner_desk_right_sid = self.find(loc.CORNER_DESK_RIGHT_SID)
        assert corner_desk_right_sid.is_displayed(), "Товар corner desk right sid не найден на странице!"


    # для large_desk
    def check_view_large_desk(self):
        large_desk = self.find(loc.LARGE_DESK)
        assert large_desk.is_displayed(), "Товар large desk не найден на странице!"


    # для desk stad with screen
    def check_view_desk_stad_with_screen(self):
        desk_stad_with_screen = self.find(loc.STAND_WITH_SCREEN_DESK)
        assert desk_stad_with_screen.is_displayed(), "Товар desk stad with screen не найден на странице!"
