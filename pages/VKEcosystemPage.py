import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class VKEcosystemPageLocators:
    HEADER_LOGO = (By.XPATH, '//*[@id="header-logo"]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.HEADER_LOGO)