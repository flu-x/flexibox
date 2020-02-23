# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class RemotechromedriverObject
#          is to connecto the remote chrome browser in the
#          docker container and execute the test cases
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from flexibox.core.logger import Logger


class RemotechromedriverObject(object):
    def __init__(self):
        self.log = Logger()

    def set_remote_chromedriver_object(self, com_exec):
        try:
            chromedriver = webdriver.Remote(command_executor=com_exec, desired_capabilities=DesiredCapabilities.CHROME)
            self.log.log_info("Remote chromedriver configuration successful")
            return chromedriver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the WebDriver configuration")
            self.log.log_error(e)
