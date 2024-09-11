import allure
from playwright.sync_api import Page

from base.pages.radio_button.radiobutton_start import RadioButtonStart
from base.pages.radio_button.radio_button_page import RadioButtonPage
from conftest import radio_button


class TestRadioButton:
    @allure.epic("Тесты потока 1")
    @allure.feature("Radio Button")
    @allure.title("Click test radio button")
    def test_radio_button(self, page: Page, radio_button: RadioButtonPage):
        RadioButtonStart.radio_button (page, radio_button)