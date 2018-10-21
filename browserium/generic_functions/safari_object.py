from selenium import webdriver
from browserium.utility.utility import Utility
from browserium.utility.os_type import OS_type
from selenium.common.exceptions import WebDriverException

class SafariDriverObject(object):
    def __init__(self):
        self.ut = Utility()
        self.ot = OS_type()

    # Get the executable binary path for safari from the config.ini file
    def set_safaridriver_object(self):
        try:
            os_environ = self.ot.os_name()
            if os_environ == "linux":
                self.ut.log_message("ERROR","Safari is not supported in Linux based operating system")
            if os_environ == "macos":
                driver = webdriver.Safari()
                self.ut.log_message("INFO","starting safari services")
                return driver
        except WebDriverException as e:
            self.ut.log_message("ERROR","There is an exception in the Web Driver configuration")
            print e