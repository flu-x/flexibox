import unittest

from flexibox.core.browser_controller import BrowserController
from flexibox.generic_functions.remotegecko_object import RemotegeckodriverObject


class Test_firefoxremote(unittest.TestCase):
    def test_firefox_type_remote(self):
        firefoxdriver = RemotegeckodriverObject()
        controller = BrowserController()
        driver = firefoxdriver.set_remote_geckodriver_object("http://localhost:4444/wd/hub")
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print(current_url)
        controller.tear_browser(driver)
