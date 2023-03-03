import time
import pytest
from random import randint
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, self.link)
        page.open()
        page.register_new_user(email=str(time.time()) + "@fakemail.org", password="test_user" + str(randint(1, 10**6)))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.message_after_adding_to_basket_contains_title()
        page.message_with_basket_total_contains_price()


@pytest.mark.need_review
@pytest.mark.parametrize("number", [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="")) for i in range(7, 10)])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_after_adding_to_basket_contains_title()
    page.message_with_basket_total_contains_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.should_not_be_goods_in_empty_basket()
    page.should_be_basket_is_empty_message()
