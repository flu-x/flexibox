from browserium.generic_functions.gecko_object import GeckoDriverObject
from browserium.generic_functions.browser_controller import BrowserController
class Test_1():
    def test_firefoxdriver_type(self):
        geckodriver = GeckoDriverObject()
        controller = BrowserController()
        driver = geckodriver.set_geckodriver_object(geckoArgs=['--headless'])
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print(current_url)

t = Test_1()
t.test_firefoxdriver_type()