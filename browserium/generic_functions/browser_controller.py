class Browser_controller(): 
    def get_url(self, driver, url):
        driver.get(url)

    def implicit_wait_time(self, driver, time):
        driver.implicitly_wait(time)

    def set_window_size(self, driver, size):
        driver.set_window_size(size)

    def get_current_url(self, driver):
        current_url = driver.current_url
        return current_url

    def get_network_requests(self, driver):
        obj_requests = driver.execute_script("return window.performance.getEntries();")
        return obj_requests

    def performance_metrics(self, driver):
        obj_overallPerformance = driver.execute_script("return performance.timing")
        return obj_overallPerformance

    def check_console_logs(self, driver):
        obj_consoleLog = driver.get_log('browser')
        return obj_consoleLog

    def get_page_source(self, driver):
        obj_pageSource = driver.page_source
        return obj_pageSource

    def get_site_cookies(self, driver):
        cookies = driver.get_cookies()
        return cookies