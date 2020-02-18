# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class ChromeDriverObject is to set the create an instance for the ChromeDriverObject class
#          to configure the chromedriver accordingly based on the environment.
# Can be used to set the chromedriver object
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from flexibox.core.logger import Logger
from flexibox.core.utility import Utility


class ChromeDriverObject(object):
    def __init__(self):
        self.ut = Utility()
        self.log = Logger()

    # Set chromedriver path
    # Pass the option 'headless' if it is needed to run chrome in headless
    # configuration
    def set_chromedriver_object(self, chromeArgs):
        try:
            chromeArgs = chromeArgs
            chromeOptions = webdriver.ChromeOptions()
            driver_path = self.ut.get_driver_path('/dependencies/dir_chromedriver/chromedriver')
            self.ut.set_executable_permission(driver_path)
            self.log.log_info("Setting executable permission to the chrome binary")
            self.log.log_info("Setting path of chromedriver")
            if not chromeArgs:
                driver = webdriver.Chrome(executable_path=driver_path)
            else:
                while '' in chromeArgs:
                    chromeArgs.remove('')
                for val in chromeArgs:
                    chromeOptions.add_argument(val)
                driver = webdriver.Chrome(executable_path=driver_path, options=chromeOptions)
            self.log.log_info("Path for chrome binary is set")
            return driver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the Web Driver configuration")
            self.log.log_error(e)
