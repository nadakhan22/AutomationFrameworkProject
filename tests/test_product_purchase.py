from selenium.webdriver.support import expected_conditions as EC
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

from pages1.index_page import IndexPage
from resources.constants import TEST_SITE_URL
from pages1.product_SonyViao_page import Product_Page_1
from pages1.cart_page import CartPage
from pages1.product2_page import ProductPage2

class TestProductPurchase():

    def test_purchase_product(self,driver):
        #Navigating to Home Page
        index_page=IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.click_on_product()#Click on Product

        #Navigating to Product 1 Page
        product_page=Product_Page_1(driver)
        product_page.add_product1_toCart()
        product_page.is_product_in_cart()

        #Navigating to Cart Page
        cart_page=CartPage(driver)
        assert cart_page.check_product_1_in_cart(),"Product 1 not added!"
        #Product 1 asserted successfully

        #Navigate to Home Page
        cart_page.click_on_home()
        index_page=IndexPage(driver)
        #Navigate to Home page
        index_page.click_on_product_2()
        #Navigate to Product 2 Page
        product_2_page= ProductPage2(driver)
        product_2_page.add_Product2_toCart()
        product_2_page.is_product2_in_cart()
        cart_page=CartPage(driver)
        assert cart_page.check_product_2_in_cart(),"Product 2 not added!"
        #Product 2 asserted in Cart successfully
        cart_page.purchase_product()
        assert cart_page.is_purchase_successful,"Purchase Unsuccessful!"
        #Purchase asserted successfully




