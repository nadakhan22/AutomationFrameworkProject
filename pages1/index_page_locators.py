from selenium.webdriver.common.by import By

class IndexPageLocators():
    SIGNUP_BUTTON=(By.ID,"signin2")
    SIGNUP_USERNAME_TEXTBOX=(By.ID,"sign-username")
    SIGNUP_PASSWORD=(By.ID,"sign-password")
    SIGNUP_SUBMIT_BUTTON=(By.XPATH,"/html/body/div[2]/div/div/div[3]/button[2]")
    LOGIN_BUTTON=(By.ID,"login2")
    USERNAME_TEXTBOX=(By.ID,"loginusername")
    PASSWORD_TEXTBOX=(By.ID,"loginpassword")
    #Change XPATH!!
    LOGIN_SUBMIT_BUTTON=(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]")

    PRODUCT_SONYVIAO_BUTTON=(By.XPATH,"/html/body/div[5]/div/div[2]/div/div[9]/div/div/h4/a")
    #HOME_PAGE_BUTTON=(By.XPATH,"//*[@id='navbarExample']/ul/li[1]/a")
    HOME_PAGE_BUTTON = (By.LINK_TEXT, "Home")
    LOG_OUT_BUTTON=(By.ID,"logout2")
    NEXT_BUTTON=(By.XPATH,"//*[@id='next2']")
    PRODUCT_NOKIALUMIA_BUTTON = (By.XPATH, "//*[@id='tbodyid']/div[2]/div/div/h4/a")
    CONTACT_BUTTON=(By.XPATH,"//*[@id='navbarExample']/ul/li[2]/a")
    CONTACT_EMAIL=(By.ID,"recipient-email")
    CONTACT_NAME=(By.ID,"recipient-name")
    CONTACT_MESSAGE=(By.ID,"message-text")
    SEND_MESSAGE_BUTTON=(By.XPATH,"//*[@id='exampleModal']/div/div/div[3]/button[2]")