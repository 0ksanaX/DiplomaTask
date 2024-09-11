import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.date_picker.date_picker_methods import DatePickerMethods
from base.pages.date_picker.date_picker_page import DatePickerPage


class DatePickerStart:
    @staticmethod
    def date_picker(page: Page, date_picker: DatePickerPage):
        errors = []
        try:
            with allure.step("Открытие страницы: date picker"):
                AuthorizationMethod.date_picker(page)

            with allure.step("Date selection"):
                DatePickerMethods.click_date_picker(date_picker)

        except AssertionError as e:
            errors.append(str(e))


