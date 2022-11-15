import os

import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture(scope='function', autouse=False)
def desktop_configuration():
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = False
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield


@pytest.fixture(scope='function', autouse=False)
def mobile_configuration():
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = False
    browser.config.window_width = 393
    browser.config.window_height = 851
    yield


def test_click_sign_in_desktop(desktop_configuration):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').should(be.visible)
    browser.element('[href="/login"]').click()


def test_click_sign_in_mobile(mobile_configuration):
    browser.open('https://github.com/')
    browser.element('[class="js-details-target Button--link Button--medium Button d-lg-none color-fg-inherit p-1"]').click()
    browser.element('[class="HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0"]').click()
