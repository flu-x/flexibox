from flexibox.core.browser_controller import BrowserController
from flexibox.generic_functions.gecko_object import GeckoDriverObject


class Test_1():
    def test_firefoxdriver_type(self):
        geckodriver = GeckoDriverObject()
        controller = BrowserController()
        driver = geckodriver.set_geckodriver_object(geckoArgs=['--headless'])
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print(current_url)
        controller.tear_browser(driver)


t = Test_1()
t.test_firefoxdriver_type()
