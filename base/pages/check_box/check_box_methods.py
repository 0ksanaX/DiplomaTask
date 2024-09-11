import allure
from playwright.sync_api import expect

from base.pages.check_box.check_box_page import CheckBoxPage
from conftest import check_box
from src.config.expectations import Wait


class CheckBoxMethods:

    @staticmethod
    def click_check_box(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)

        try:
            with allure.step("Registration forms"):
                check_box.expand.click()
                check_box.home.click()
                check_box.collapse.click()




        except AssertionError as e:
            errors.append(str(e))