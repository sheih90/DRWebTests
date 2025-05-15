from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]') # или (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '// *[@data-l="t,sign_in"]')
    LOGIN_FIELD_PASSWORD = (By.XPATH, '//*[@id="field_password"]')
    LOGIN_BUTTON_QR = (By.XPATH, '// *[@data-l="t,get_qr"]')
    LOGIN_TAB = (By.XPATH, '//*[data-l="t,login_tab"]')
    LOGIN_TAB_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_LINK_RESTORE = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_BUTTON_REGISTER = (By.XPATH, '//*[@tsid="login-block21_link_ffa6bf"]')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BUTTON_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')

class LoginPageHelper(BasePage):
    pass