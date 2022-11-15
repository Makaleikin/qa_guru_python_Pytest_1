from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.fixture(scope='function')
def app(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("app", [(393, 851), (1920, 1080)], ids=['Mobile', 'Desktop'], indirect=True)
def test_with_param(app):

    if (browser.config.window_width == 393) and (browser.config.window_height == 851):
        pytest.skip("This test running for mobile browser")

    browser.open('https://github.com/')
    browser.element('[href="/login"]').should(be.visible)
    browser.element('[href="/login"]').click()
