from browserium.generic_functions.chrome_object import ChromeDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
# from browserium.generic_functions.logger import Logstash
from time import sleep

class Test_1():
    def test_chromedriver_type1(self):
        chromedriver = ChromeDriverObject()
        controller = Browser_controller()
        driver = chromedriver.set_chromedriver_object()
        # log = Logstash()
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
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
        # log.logstash_type("INFO","Test")
        # log.logstash_type("ERROR","Test")
        # log.logstash_type("WARNING","Test")
        driver.quit()

    def test_chromedriver_type2(self):
        chromedriver = ChromeDriverObject()
        controller = Browser_controller()
        driver = chromedriver.set_chromedriver_object("--headless")
        # log = Logstash()
        controller.get_url(driver, "https://www.google.co.in")
        controller.implicit_wait_time(driver, 4)
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
        # log.logstash_type("INFO","Test")
        # log.logstash_type("ERROR","Test")
        # log.logstash_type("WARNING","Test")
        driver.quit()

t = Test_1()
t.test_chromedriver_type1()
t.test_chromedriver_type2()