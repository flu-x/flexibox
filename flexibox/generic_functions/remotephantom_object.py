# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class RemotephantomdriverObject
#          is to connect to the remote phantom browser in the
#          docker container and execute the test cases
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from flexibox.core.logger import Logger


class RemotephantomdriverObject(object):
    def __init__(self):
        self.log = Logger()

    def set_remote_phantomdriver_object(self, com_exec, capabilities):
        try:
            phantomdriver = webdriver.Remote(
                command_executor=com_exec,
                # desired_capabilities={
                #     'waitForReady': True,
                #     'applicationType': 'Web',
                #     'takesScreenshot': False,
                #     'reuseExistingSession': True
                # }
                desired_capabilities=capabilities
            )
            self.log.log_info("Remote geckodriver configuration successful")
            return phantomdriver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the WebDriver configuration")
            self.log.log_error(e)
