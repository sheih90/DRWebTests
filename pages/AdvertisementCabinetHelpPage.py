import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class AdvertisementCabinetHelpLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')

class AdvertisementCabinetHelpHelper(BasePage):
    def __init__(self, driver):
            self.driver = driver
            self.check_page()

    def check_page(self):
        self.find_element(AdvertisementCabinetHelpLocators.TITLE)
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()