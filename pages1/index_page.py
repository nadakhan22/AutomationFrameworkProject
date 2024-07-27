import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages1.base_page import BasePage
from pages1.index_page_locators import IndexPageLocators
from resources.constants import *
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException



# index page
class IndexPage(BasePage):
    def signup_new_user(self, username_password):

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNUP_BUTTON).click()

        username_textbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(IndexPageLocators.SIGNUP_USERNAME_TEXTBOX)
        )
        username_textbox.send_keys(username_password[0])

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNUP_PASSWORD).send_keys(
            username_password[1])

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNUP_SUBMIT_BUTTON).click()

        try:
            # Attempt to find and click the submit button again
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNUP_SUBMIT_BUTTON).click()

        except NoAlertPresentException:
            # Expected behavior after signup, no alert should be present
            print("No alert was expected after signup.")


        except UnexpectedAlertPresentException as e:

            # Attempt to handle the alert directly

            try:

                alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                alert.accept()  # Or alert.dismiss() depending on the desired action

            except NoAlertPresentException:

                print("UnexpectedAlertPresentException raised, but no alert was found.")

            except Exception as ex:

                print(f"An error occurred while handling the alert: {ex}")


    def user_login(self,username_password):

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.LOGIN_BUTTON).click()

        login_username_textbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(IndexPageLocators.USERNAME_TEXTBOX)
        )
        login_username_textbox.send_keys(username_password[0])

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.PASSWORD_TEXTBOX).send_keys(
            username_password[1])



        try:
            # Attempt to find and click the submit button again
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.LOGIN_SUBMIT_BUTTON).click()

        except NoAlertPresentException:
            # Expected behavior after signup, no alert should be present
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



    def user_logout(self):
        #self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.LOG_OUT_BUTTON).click()
        login_button=WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(IndexPageLocators.LOGIN_BUTTON)
        )

        login_button_text=login_button.text
        if login_button_text in LOGIN_BUTTON_TEXT:
            return True
        else:
            return False

    def click_on_product(self):

        product1_button=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(IndexPageLocators.PRODUCT_SONYVIAO_BUTTON))

        product1_button.click()

    def click_on_product_2(self):
        product2_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(IndexPageLocators.PRODUCT_NOKIALUMIA_BUTTON))

        product2_button.click()

    def click_on_contact(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.CONTACT_BUTTON).click()
        contact_email = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(IndexPageLocators.CONTACT_EMAIL)
        )
        contact_email.send_keys(CONTACT_EMAIL)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.CONTACT_NAME).send_keys(CONTACT_NAME)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.CONTACT_MESSAGE).send_keys(MESSAGE)
        try:
            # Attempt to find and click the submit button again
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SEND_MESSAGE_BUTTON).click()

        except UnexpectedAlertPresentException as e:
                alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                alert_text = alert.text
                alert.accept()  # Or alert.dismiss() depending on the desired action



