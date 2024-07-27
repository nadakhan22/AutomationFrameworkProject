import time
from pages1.product_SonyViao_page_locators import ProductPageLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from pages1.base_page import BasePage
from pages1.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, TEST_SITE_URL, LOGIN_BUTTON_TEXT
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.common.alert import Alert

class Product_Page_1(BasePage):
 def add_product1_toCart(self):

  try:

   self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ProductPageLocators.ADD_TO_CART_BUTTON_1).click()

  except NoAlertPresentException:

   print("No alert was expected after signup.")


  except UnexpectedAlertPresentException as e:

   # Attempt to handle the alert directly

   try:

    alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    alert_text = alert.text

    alert.accept()  # Or alert.dismiss() depending on the desired action

   except NoAlertPresentException:

    # Handle the case where no alert was found

    print("UnexpectedAlertPresentException raised, but no alert was found.")

   except Exception as ex:

    # Handle any other exceptions that might occur

    print(f"An error occurred while handling the alert: {ex}")


 def is_product_in_cart(self):
  self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ProductPageLocators.CART_BUTTON).click()

