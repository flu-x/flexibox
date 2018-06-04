from browserium.generic_functions.opera_object import OperaDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
from time import sleep

class Test_Opera():
    def test_operadriver_type1(self):
        operadriver = OperaDriverObject()
        controller = Browser_controller()
        driver = operadriver.set_operadriver_object()
        controller.implicit_wait_time(driver, 4)
        controller.get_url(driver, "https://www.google.co.in")
        current_url = controller.get_current_url(driver)
        print current_url
        print driver.title

t = Test_Opera()
t.test_operadriver_type1()