import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetHelpPage import AdvertisementCabinetHelpHelper

BASE_URL = "https://ok.ru/help"

@allure.suite('Проверка страницы Помощь')
@allure.title('Проверка перехода в рекламный кабинет')
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTICEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)


