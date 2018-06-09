from browserium.utility.utility import Utility
class Browser_controller(Utility): 
    def get_url(self, driver, url):
        driver.get(url)
        self.log_message("INFO", "Fetching URL")

    def implicit_wait_time(self, driver, time):
        driver.implicitly_wait(time)
        self.log_message("INFO", "Applying implicit wait")

    def set_window_size(self, driver, height, width):
        window_height = int(height)
        window_width = int(width)
        driver.set_window_size(window_height, window_width)
        self.log_message("INFO", "Setting window size")

    def get_current_url(self, driver):
        current_url = driver.current_url
        self.log_message("INFO", "Fetching the current URL of the page")
        return current_url

    def get_network_requests(self, driver):
        obj_requests = driver.execute_script("return window.performance.getEntries();")
        self.log_message("INFO", "Fetching all network requests")
        return obj_requests

    def performance_metrics(self, driver):
        obj_overallPerformance = driver.execute_script("return performance.timing")
        self.log_message("INFO", "Fetching current page performance data")
        return obj_overallPerformance

    def check_console_logs(self, driver):
        obj_consoleLog = driver.get_log('browser')
        self.log_message("INFO", "Fetching console logs")
        return obj_consoleLog

    def get_page_source(self, driver):
        obj_pageSource = driver.page_source
        self.log_message("INFO", "Fetching page source")
        return obj_pageSource

    def get_site_cookies(self, driver):
        cookies = driver.get_cookies()
        self.log_message("INFO", "Fetching all cookies")
        return cookies