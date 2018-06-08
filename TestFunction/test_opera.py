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
        controller.set_window_size(driver, "1440", "900")
        network_requests = controller.get_network_requests(driver)
        print network_requests
        page_source_data = controller.get_page_source(driver)
        print page_source_data
        console_data = controller.check_console_logs(driver)
        print console_data
        performance = controller.performance_metrics(driver)
        print performance
        site_cookies = controller.get_site_cookies(driver)
        print site_cookies
        current_url = controller.get_current_url(driver)
        print current_url

t = Test_Opera()
t.test_operadriver_type1()