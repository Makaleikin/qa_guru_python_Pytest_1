import os

import pytest
from selene.support.shared import browser


# @pytest.fixture(scope='function', autouse=False)
# def desktop_configuration():
#     browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#     browser.config.hold_browser_open = False
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     yield
#
#
# @pytest.fixture(scope='function', autouse=False)
# def mobile_configuration():
#     browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#     browser.config.hold_browser_open = False
#     browser.config.window_width = 393
#     browser.config.window_height = 851
#     yield