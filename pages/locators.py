from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#register_form>.form-group:nth-child(3)>div>input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#register_form>.form-group:nth-child(4)>div>input")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#register_form>.form-group:nth-child(5)>div>input")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE = (By.CSS_SELECTOR, ".product_main h1")
    ADDING_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages>div:last-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")
