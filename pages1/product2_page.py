import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages1.base_page import BasePage
from pages1.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, LOGIN_BUTTON_TEXT
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException
from pages1.product2_page_locators import Product2PageLocators


class ProductPage2(BasePage):

    def add_Product2_toCart(self):

        try:

            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                 Product2PageLocators.ADD_TO_CART_BUTTON).click()

        except NoAlertPresentException:

            print("No alert was expected after signup.")


        except UnexpectedAlertPresentException as e:

            # Attempt to handle the alert directly

            try:

                alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())

                alert_text = alert.text

                alert.accept()  # Or alert.dismiss() depending on the desired action

            except NoAlertPresentException:

                # Handle the case where no alert was found

                print("UnexpectedAlertPresentException raised, but no alert was found.")

            except Exception as ex:

                # Handle any other exceptions that might occur

                print(f"An error occurred while handling the alert: {ex}")

    def is_product2_in_cart(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, Product2PageLocators.CART_BUTTON).click()
