from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from browserium.utility.utility import Utility

class PhantomDriverObject(Utility):
    # Set chromedriver path
    # Pass the option 'headless' if it is needed to run chrome in headless
    # configuration
    def set_phantomdriver_object(self):
        try:
            driver_path = self.get_driver_path('/dependencies/dir_phantomjsdriver/phantomjsdriver/bin/phantomjs')
            self.set_executable_permission(driver_path)
            self.log_message("INFO","setting executable permission to the phantom binary")
            driver = webdriver.PhantomJS(executable_path=driver_path)
            self.log_message("INFO","Path for phantom binary is set")
            return driver
        except WebDriverException as e:
            self.log_message("ERROR","There is an exception in the Web Driver configuration")
            self.log.log_error(e)