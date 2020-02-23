import unittest

from flexibox.core.browser_controller import BrowserController
from flexibox.generic_functions.chrome_object import ChromeDriverObject
from flexibox.generic_functions.remotechrome_object import RemotechromedriverObject


class Test_chromestandalone(unittest.TestCase):
    def test_chromedriver_type_standalone(self):
        chromedriver = ChromeDriverObject()
        controller = BrowserController()
        driver = chromedriver.set_chromedriver_object(chromeArgs=['--headless'])
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print(current_url)
        controller.tear_browser(driver)
