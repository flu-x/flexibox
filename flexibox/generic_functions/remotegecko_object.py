# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class RemotegeckodriverObject
#          is to connect to the remote firefox browser in the
#          docker container and execute the test cases
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from flexibox.core.logger import Logger


class RemotegeckodriverObject(object):
    def __init__(self):
        self.log = Logger()

    def set_remote_geckodriver_object(self, com_exec):
        try:
            geckodriver = webdriver.Remote(command_executor=com_exec, desired_capabilities=DesiredCapabilities.FIREFOX)
            self.log.log_info("Remote geckodriver configuration successful")
            return geckodriver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the WebDriver configuration")
            self.log.log_error(e)
