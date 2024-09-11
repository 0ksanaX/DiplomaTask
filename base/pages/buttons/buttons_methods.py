from turtle import right

import allure

from playwright._impl._helper import MouseButton

from base.pages.buttons.buttons_page import ButtonsPage
from src.config.expectations import Wait


class ButtonsMethods:

    @staticmethod
    def double_click_buttons(buttons: ButtonsPage):
        errors = []
        Wait.set_page(buttons.page)

        try:
            with allure.step("double click Buttons"):
                buttons.dclick_me.double_click()

            return buttons.dclick_message.is_visible()

        except AssertionError as e:
            errors.append(str(e))