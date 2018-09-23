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
        driver.quit()

    def test_geckodriver_type2(self):
        geckodriver = GeckoDriverObject()
        controller = Browser_controller()
        driver = geckodriver.set_geckodriver_object('--headless')
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
        controller.set_window_size(driver, "1440", "900")
        network_requests = controller.get_network_requests(driver)
        print network_requests
        page_source_data = controller.get_page_source(driver)
        print page_source_data
        performance = controller.performance_metrics(driver)
        print performance
        site_cookies = controller.get_site_cookies(driver)
        print site_cookies
        current_url = controller.get_current_url(driver)
        print current_url
        driver.quit()

t = Test_2()
# t.test_geckodriver_type1()
t.test_geckodriver_type2()