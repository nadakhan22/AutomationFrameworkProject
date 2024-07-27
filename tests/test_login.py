import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

from pages1.index_page import IndexPage
from resources.constants import TEST_SITE_URL

class TestLogin:

    #Test a New User Sign-Up
    def test_new_user_signup(self,driver,username_password):
        index_page=IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.signup_new_user(username_password)
        # assert index_page.is_signup_successful(),"Sign-Up Failed"

    def test_user_login(self,driver,username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.user_login(username_password)
        time.sleep(5)

    def test_user_logout(self,driver,username_password):
        index_page=IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.user_login(username_password)
        assert index_page.user_logout(),"Logout failed"





