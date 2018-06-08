from browserium.generic_functions.gecko_object import GeckoDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
from time import sleep

class Test_2():
    def test_geckodriver_type1(self):
        geckodriver = GeckoDriverObject()
        controller = Browser_controller()
        driver = geckodriver.set_geckodriver_object()
        controller.implicit_wait_time(driver, 4)
        controller.get_url(driver, "https://www.google.co.in")
        current_url = controller.get_current_url(driver)
        print current_url
        print driver.title

    def test_geckodriver_type2(self):
        geckodriver = GeckoDriverObject()
        controller = Browser_controller()
        driver = geckodriver.set_geckodriver_object('--headless')
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print current_url
        print driver.title

t = Test_2()
t.test_geckodriver_type1()
t.test_geckodriver_type2()