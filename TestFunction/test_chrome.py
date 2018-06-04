from browserium.generic_functions.chrome_object import ChromeDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
from time import sleep

class Test_1():
    def test_chromedriver_type1(self):
        chromedriver = ChromeDriverObject()
        controller = Browser_controller()
        driver = chromedriver.set_chromedriver_object()
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print current_url

    def test_chromedriver_type2(self):
        chromedriver = ChromeDriverObject()
        controller = Browser_controller()
        driver = chromedriver.set_chromedriver_object("--headless")
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        current_url = controller.get_current_url(driver)
        print current_url

t = Test_1()
t.test_chromedriver_type1()
t.test_chromedriver_type2()