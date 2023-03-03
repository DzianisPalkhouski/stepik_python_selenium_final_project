from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def message_after_adding_to_basket_contains_title(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE).text
        adding_message = self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE).text
        assert title == adding_message, f"Expected {title} == {adding_message}"

    def message_with_basket_total_contains_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert price == price_message, "Message with_basket_total_does_not_contain_price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message does not disappear"
