from pages.locators.office_software_locators import SoftwareLocators as loc
from pages.base_page import BasePage


class OfficeSoftwareText(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'


    def check_benelux_is(self, expected_text):
        dropdown_is = self.find(loc.DROPDOWN_BTN)
        dropdown_benelux = dropdown_is.text
        assert dropdown_benelux == expected_text, \
            f"Ожидали '{expected_text}', получили '{dropdown_benelux}'"


    def check_text_title_design_software_is(self, expected_text):
        design_software_title = self.find(loc.DESIGN_SOFTWARE)
        design_software = design_software_title.text
        assert design_software == expected_text, \
            f"Ожидали '{expected_text}', получили '{design_software}'"


    def check_text_h1_product_details_is(self, expected_text):
        h1_product_details = self.find(loc.H1_OFFICE_DESIGN_SOFTWARE)
        actual_text = h1_product_details.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_h3_product_price_is(self, expected_text):
        product_price = self.find(loc.PRODUCT_PRICE)
        actual_text = product_price.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_terms_and_conditions_is(self, expected_text):
        terms_ann_conditions = self.find(loc.TERMS_AND_CONDITIONS)
        actual_text = terms_ann_conditions.text
        assert actual_text == expected_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"


    def check_text_money_back_is(self, expected_text):
        money_back = self.find(loc.MONEY_BACK_GUARANTEE)
        actual_text = money_back.get_attribute('textContent').strip()
        assert expected_text in actual_text, \
            f"Ожидали '{expected_text}', получили '{actual_text}'"
