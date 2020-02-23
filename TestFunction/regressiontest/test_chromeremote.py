import unittest

from flexibox.core.browser_controller import BrowserController
from flexibox.generic_functions.remotechrome_object import RemotechromedriverObject


class Test_chromeremote(unittest.TestCase):
    def test_chromedriver_type_remote(self):
        chromedriver = RemotechromedriverObject()
        controller = BrowserController()
        driver = chromedriver.set_remote_chromedriver_object("http://localhost:4444/wd/hub")
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print(current_url)
        controller.tear_browser(driver)
