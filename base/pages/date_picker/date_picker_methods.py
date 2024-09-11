import time

import allure

from base.pages.date_picker.date_picker_page import DatePickerPage
from src.config.expectations import Wait


class DatePickerMethods:

    @staticmethod
    def click_date_picker(date_picker: DatePickerPage):
        errors = []
        Wait.set_page(date_picker.page)

        try:
            with allure.step("date picker"):
                date_picker.select_date.click()
                date_picker.open_selector.click()
                date_picker.select_month.click()
                time.sleep(20)



        except AssertionError as e:
            errors.append(str(e))



