from selenium import webdriver
from browserium.utility.logger import Logger
from browserium.utility.utility import Utility
from browserium.utility.os_type import OS_type
from selenium.common.exceptions import WebDriverException

class SafariDriverObject(object):
    def __init__(self):
        self.log = Logger()
        self.ut = Utility()
        self.ot = OS_type()

    # Get the executable binary path for safari from the config.ini file
    def set_safaridriver_object(self):
        try:
            os_environ = self.ot.os_name()
            if os_environ == "linux":
                self.log.log_error("Safari is not supported in Linux based operating system")
            if os_environ == "macos":
                driver = webdriver.Safari()
                self.log.log_info("Starting safari services")
                return driver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the Web Driver configuration")
            self.log.log_error(e)