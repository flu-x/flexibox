from browserium.utility.utility import Utility
from browserium.utility.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException

from time import sleep

class BrowserController(object):

    def __init__(self):
        self.ut = Utility()
        self.log = Logger()

    def get_url(self, driver, url):
        driver.get(url)
        self.log.log_info("Fetching URL")

    def implicit_wait_time(self, driver, time):
        driver.implicitly_wait(time)
        self.log.log_info("Applying implicit wait")

    def set_window_size(self, driver, height, width):
        window_height = int(height)
        window_width = int(width)
        driver.set_window_size(window_height, window_width)
        self.log.log_info("Setting window size")

    def get_current_url(self, driver):
        current_url = driver.current_url
        self.log.log_info("Fetching the current URL of the page")
        return current_url

    def get_network_requests(self, driver):
        obj_requests = driver.execute_script("return window.performance.getEntries();")
        self.log.log_info("Fetching all network requests")
        return obj_requests

    def performance_metrics(self, driver):
        obj_overallPerformance = driver.execute_script("return performance.timing")
        self.log.log_info("Fetching current page performance data")
        return obj_overallPerformance

    def check_console_logs(self, driver):
        obj_consoleLog = driver.get_log('browser')
        self.log.log_info("Fetching console logs")
        return obj_consoleLog

    def get_page_source(self, driver):
        obj_pageSource = driver.page_source
        self.log.log_info("Fetching page source")
        return obj_pageSource

    def get_site_cookies(self, driver):
        cookies = driver.get_cookies()
        self.log.log_info("Fetching all cookies")
        return cookies

    def apply_explicit_wait_time(self, sleepTime):
        sleep(sleepTime)
        self.log.log_info("Applying explicit wait time")

    def maximize_window(self, driver):
        driver.maximize_window()
        self.log.log_info("Window maximized")

    def apply_fluent_wait(self, driver, fluent_wait_time):
        wait = WebDriverWait(
                    driver,
                    fluent_wait_time,
                    poll_frequency=1,
                    ignored_exceptions=[
                        NoSuchElementException,
                        ElementNotVisibleException,
                        ElementNotSelectableException
                    ]
                )
        self.log.log_info("Applying fluent wait")
        return wait

    def tear_browser(self, driver):
        driver.quit()
        self.log.log_info("Quit browser session")