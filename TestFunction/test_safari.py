from browserium.generic_functions.safari_object import SafariDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
from time import sleep

class Test_1():
    def test_safaridriver_type1(self):
        safaridriver = SafariDriverObject()
        controller = Browser_controller()
        driver = safaridriver.set_safaridriver_object()
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print current_url
        print driver.title
        driver.quit()

t = Test_1()
t.test_safaridriver_type1()