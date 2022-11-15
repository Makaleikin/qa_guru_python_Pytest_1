import pytest
from selene.support.conditions import be
from selene.support.shared import browser


@pytest.mark.parametrize(['browser_width', 'browser_height'],
                         [(1920, 1080), (393, 851)],
                         ids=['Desktop', 'Mobile'],
                         )
def test_with_param(browser_width, browser_height):
    browser.config.window_width = browser_width
    browser.config.window_height = browser_height

    browser.open('https://github.com/')

    if (browser_width == 1920) and (browser_height == 1024):
        browser.element('[href="/login"]').should(be.visible)
        browser.element('[href="/login"]').click()
    elif (browser_width == 393) and (browser_height == 851):
        browser.element(
            '[class="js-details-target Button--link Button--medium Button d-lg-none color-fg-inherit p-1"]').click()
        browser.element(
            '[class="HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block '
            'border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0"]').click()
