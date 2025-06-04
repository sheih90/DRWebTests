import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.AdvertisementCabinetHelpPage import AdvertisementCabinetHelpHelper

BASE_URL = "https://ok.ru/help"

@allure.suite('Проверка страницы Помощь')
@allure.title('Проверка перехода в рекламный кабинет')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTICEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)


