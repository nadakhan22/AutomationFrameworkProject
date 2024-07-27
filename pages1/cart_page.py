import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages1.base_page import BasePage
from pages1.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, LOGIN_BUTTON_TEXT
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException
from pages1.cart_page_locators import CartPageLocators
from resources.constants import *
class CartPage(BasePage):

    def check_product_1_in_cart(self):
        product_title = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CartPageLocators.PRODUCT_1_TITLE)
        )
        product_title=product_title.text
        product_price=self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CartPageLocators.PRODUCT_1_PRICE).text

        if product_title in PRODUCT_1_TITLE and product_price in PRODUCT_1_PRICE:
           return True
        else:
            return False

    def click_on_home(self):

        home_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CartPageLocators.HOME_BUTTON)
        )
        home_button.click()


    def check_product_2_in_cart(self):


        product_title= WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CartPageLocators.PRODUCT_2_TITLE)
        )
        product_title=product_title.text

        product_price = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CartPageLocators.PRODUCT_2_PRICE)
        )
        product_price=product_price.text

        if product_title in PRODUCT_2_TITLE and product_price in PRODUCT_2_PRICE:
           return True
        else:
            return False

    def purchase_product(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CartPageLocators.PLACE_ORDER_BUTTON).click()
        name_textbox = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(CartPageLocators.ORDER_NAME)
        )
        name_textbox.send_keys(ORDER_NAME)

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CartPageLocators.ORDER_COUNTRY).send_keys(
            ORDER_COUNTRY)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CartPageLocators.ORDER_CITY).send_keys(
            ORDER_CITY)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CartPageLocators.ORDER_CREDIT_CARD).send_keys(
            ORDER_CC)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CartPageLocators.ORDER_CC_MONTH).send_keys(
            ORDER_CC_MONTH)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CartPageLocators.ORDER_CC_YEAR).send_keys(
            ORDER_CC_YEAR)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CartPageLocators.ORDER_PURCHASE_BUTTON).click()

    def is_purchase_successful(self):


        success_message= WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(CartPageLocators.ORDER_PLACED_MESSAGE)
        )

        success_message=success_message.text

        if success_message in SUCCESS_MESSAGE:
            return True
        else:
            return False


