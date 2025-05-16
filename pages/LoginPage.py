from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]') # или (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '// *[@data-l="t,sign_in"]')
    LOGIN_FIELD_PASSWORD = (By.XPATH, '//*[@id="field_password"]')
    LOGIN_BUTTON_QR = (By.XPATH, '// *[@data-l="t,get_qr"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_TAB_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_LINK_RESTORE = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_BUTTON_REGISTER = (By.XPATH, '//*[@tsid="login-block21_link_ffa6bf"]') # или (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BUTTON_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_FIELD_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_QR)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_TAB_QR)
        self.find_element(LoginPageLocators.LOGIN_LINK_RESTORE)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_REGISTER)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_VK)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_MAIL)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_YANDEX)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def send_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys('test@t.ru')