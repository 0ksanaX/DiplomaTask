from playwright.sync_api import Page

from base.page_factory.button import Button



class DatePickerPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Date picker"""

        self.select_date = Button(page, locator='//*[@id="datePickerMonthYearInput"]', name='Pick date selection')
        self.open_selector = Button(page, locator='//*[starts-with(@class="react-datepicker__month-select"]', name='Open date selector')
        self.select_month = Button(page, locator='//*[value="5"]', name='Choose February')






