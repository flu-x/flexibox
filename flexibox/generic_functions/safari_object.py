# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class ChromeDriverObject is to set the create an instance for the OperaDriverObject class
#          to configure the geckodriver accordingly based on the environment.
# Can be used to set the operadriver object
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from flexibox.core.logger import Logger
from flexibox.core.utility import Utility
from flexibox.utility.os_type import OS_type


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
