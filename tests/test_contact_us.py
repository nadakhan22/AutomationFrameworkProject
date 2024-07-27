
from pages1.index_page import IndexPage
from resources.constants import TEST_SITE_URL

class TestContactUs:

    def test_contact_us(self,driver):
        index_page=IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.click_on_contact()
        #Function to click on contact-us



