from playwright.sync_api import Page
from base.page_factory.button import Button
from base.page_factory.input import Input


class TextBoxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: text box"""
        self.full_name = Input(page, locator='//*[@id="userName"]', name='Full Name')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Email')
        self.current_address = Input(page, locator='//*[@id="currentAddress"]', name='Current address')
        self.permanent_address = Input(page, locator='//*[@id="permanentAddress"]', name='Current address')
        self.submit = Button(page, locator='//*[@id="submit"]', name='Submit')

        """Ожидания"""
        self.Wait_full_name = '//*[@id="userName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_current_address = '//*[@id="currentAddress"]'


        """Текст"""
        self.Name_text = 'Ksenia Klinkova'