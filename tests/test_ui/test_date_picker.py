import allure
from playwright.sync_api import Page

from base.pages.date_picker.date_picker_page import DatePickerPage
from base.pages.date_picker.datepicker_start import DatePickerStart
from conftest import date_picker


class TestDatePicker:

    @allure.epic("Тесты потока 6")
    @allure.feature("Date Picker")
    @allure.title("Date picker test")
    def test_date_picker(self, page: Page, date_picker: DatePickerPage):
        DatePickerStart.date_picker(page, date_picker)