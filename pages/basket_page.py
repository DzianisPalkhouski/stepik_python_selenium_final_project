from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE),\
            "Message about empty basket is not presented"

    def should_not_be_goods_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "Basket contains goods"
