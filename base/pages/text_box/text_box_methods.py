import allure

from base.pages.text_box.text_box_page import TextBoxPage
from src.config.expectations import Wait


class TextBoxMethods:

    @staticmethod
    def fill_text_input(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)

        try:
            with allure.step("Registration forms"):
                text_box.full_name.fill(text_box.Name_text)
                text_box.email.fill('klinkova@gmail.com')
                text_box.current_address.fill('Str. Starokubanskaya 114')
                text_box.permanent_address.fill('Krasnodar')
                text_box.submit.click()


        except AssertionError as e:
            errors.append(str(e))