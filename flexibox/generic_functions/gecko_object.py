# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class ChromeDriverObject is to set the create an instance for the GeckoDriverObject class
#          to configure the geckodriver accordingly based on the environment.
# Can be used to set the chromedriver object
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

from flexibox.core.logger import Logger
from flexibox.core.utility import Utility


class GeckoDriverObject(object):
    def __init__(self):
        self.ut = Utility()
        self.log = Logger()

    # Set geckodriver path
    # Pass the option 'headless' if it is needed to run gecko in headless
    # configuration

    def set_geckodriver_object(self, geckoArgs=None):
        try:
            geckoArgs = geckoArgs
            firefoxOptions = Options()
            driver_path = self.ut.get_driver_path('/dependencies/dir_geckodriver/geckodriver')
            self.log.log_info("Setting path of geckodriver")
            if not geckoArgs:
                driver = webdriver.Firefox(executable_path=driver_path)
            else:
                while '' in geckoArgs:
                    geckoArgs.remove()
                for val in geckoArgs:
                    firefoxOptions.add_argument(val)
                driver = webdriver.Firefox(executable_path=driver_path, firefox_options=firefoxOptions)
            return driver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the Web Driver configuration")
            self.log.log_error(e)
