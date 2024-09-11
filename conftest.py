import pytest
import time
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from src.config.playwright import PlaywrightConfig
from playwright.sync_api import Page, sync_playwright, Browser


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
def modal_dialogs(page: Page) -> ModalDialogsPage:
    return ModalDialogsPage(page)

