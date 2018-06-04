from browserium.generic_functions.phantom_object import PhantomDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
from time import sleep

class Test_1():
    def test_phantomdriver_type1(self):
        phantomdriver = PhantomDriverObject()
        controller = Browser_controller()
        driver = phantomdriver.set_phantomdriver_object()
        controller.implicit_wait_time(driver, 4)
        controller.get_url(driver, "https://www.google.co.in")
        current_url = controller.get_current_url(driver)
        print current_url

t = Test_1()
t.test_phantomdriver_type1()