from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from flexibox.core.logger import Logger
from flexibox.core.utility import Utility


class PhantomDriverObject(object):
    def __init__(self):
        self.ut = Utility()
        self.log = Logger()

    # Set chromedriver path
    # Pass the option 'headless' if it is needed to run chrome in headless
    # configuration

    def set_phantomdriver_object(self):
        try:
            driver_path = self.ut.get_driver_path('/dependencies/dir_phantomjsdriver/phantomjsdriver/bin/phantomjs')
            self.ut.set_executable_permission(driver_path)
            self.log.log_info("Setting executable permission to the phantom binary")
            driver = webdriver.PhantomJS(executable_path=driver_path)
            self.log.log_info("Path for phantom binary is set")
            return driver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the Web Driver configuration")
