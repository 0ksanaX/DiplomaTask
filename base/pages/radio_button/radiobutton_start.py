import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.radio_button.radio_button_methods import RadioButtonMethods
from base.pages.radio_button.radio_button_page import RadioButtonPage


class RadioButtonStart:
    @staticmethod
    def radio_button(page: Page, radio_button: RadioButtonPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.radio_button(page)

            with allure.step("Ввод данных пользователя"):
                RadioButtonMethods.click_radio_button(radio_button)

        except AssertionError as e:
            errors.append(str(e))


