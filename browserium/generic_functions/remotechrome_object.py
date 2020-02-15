# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class RemotechromedriverObject
#          is to connecto the remote chrome browser in the 
#          docker container and execute the test cases

from selenium import webdriver
from browserium.core.logger import Logger
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class RemotechromedriverObject(object):

    def __init__(self):
        self.log = Logger()

    def set_remote_geckodriver_object(self, com_exec):
        try:
            chromedriver = webdriver.Remote(
                command_executor = com_exec,
                desired_capabilities = DesiredCapabilities.CHROME
            )
            self.log.log_info("Remote chromedriver configuration successful")
            return chromedriver
        except WebDriverException e:
            self.log.log_error("There is an exception in the WebDriver configuration")