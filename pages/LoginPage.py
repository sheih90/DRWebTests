import allure

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
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.XPATH, '//*[@name="st.go_to_recovery"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
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

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Запоняем поле логин')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Запоняем поле пароль')
    def type_password(self, password):
        self.find_element(LoginPageLocators.LOGIN_FIELD_PASSWORD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()