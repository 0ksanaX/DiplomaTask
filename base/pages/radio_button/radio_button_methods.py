import allure

from base.pages.radio_button.radio_button_page import RadioButtonPage
from src.config.expectations import Wait


class RadioButtonMethods:

    @staticmethod
    def click_radio_button(radio_button: RadioButtonPage):
        errors = []
        Wait.set_page(radio_button.page)

        try:
            with allure.step("Radio Buttons"):
                radio_button.yes.click()
                radio_button.impressive.click()
                radio_button.yes.click()
                radio_button.impressive.click()


        except AssertionError as e:
            errors.append(str(e))