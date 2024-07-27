from selenium.webdriver.common.by import By

class CartPageLocators:

    PRODUCT_1_TITLE=(By.XPATH,"//*[@id='tbodyid']/tr/td[2]")
    PRODUCT_1_PRICE=(By.XPATH,"//*[@id='tbodyid']/tr/td[3]")
    TOTAL_PRICE=(By.XPATH,"//*[@id='totalp']")
    HOME_BUTTON=(By.XPATH,"//*[@id='navbarExample']/ul/li[1]/a")
    PRODUCT_2_TITLE=(By.XPATH,"//*[@id='tbodyid']/tr[2]/td[2]")
    PRODUCT_2_PRICE=(By.XPATH,"//*[@id='tbodyid']/tr[2]/td[3]")
    PLACE_ORDER_BUTTON =(By.XPATH,"//*[@id='page-wrapper']/div/div[2]/button")
    ORDER_PRICE=(By.XPATH,"/html/body/div[10]/p/text()[2]")
    ORDER_NAME=(By.ID,"name")
    ORDER_COUNTRY=(By.ID,"country")
    ORDER_CITY=(By.ID,"city")
    ORDER_CREDIT_CARD=(By.ID,"card")
    ORDER_CC_MONTH=(By.ID,"month")
    ORDER_CC_YEAR=(By.ID,"year")
    ORDER_PURCHASE_BUTTON = (By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
    ORDER_PLACED_MESSAGE = (By.XPATH, "/html/body/div[10]/h2")
    ORDER_SUCCESS_OK_BUTTON=(By.XPATH,"/html/body/div[10]/div[7]/div/button")
