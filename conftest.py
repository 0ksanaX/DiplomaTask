import time

import pytest
from playwright.sync_api import Page, sync_playwright, Browser

from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.check_box.check_box_page import CheckBoxPage
from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.text_box.text_box_page import TextBoxPage
from src.config.playwright import PlaywrightConfig


@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page(viewport=PlaywrightConfig.PAGE_VIEWPORT_SIZE)
        yield page
        time.sleep(10)
        browser.close()


def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if PlaywrightConfig.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=PlaywrightConfig.IS_HEADLESS,
        slow_mo=PlaywrightConfig.SLOW_MO
    )


@pytest.fixture(scope='function')
def text_box(page: Page) -> TextBoxPage:
    return TextBoxPage(page)
@pytest.fixture(scope='function')
def radio_button(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)
@pytest.fixture(scope='function')
def check_box(page: Page) -> CheckBoxPage:
    return CheckBoxPage(page)
@pytest.fixture(scope='function')
def buttons(page: Page) -> ButtonsPage:
    return ButtonsPage(page)

