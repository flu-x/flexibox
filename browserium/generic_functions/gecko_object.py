from selenium import webdriver
from browserium.utility.logger import Logger
from browserium.utility.utility import Utility
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

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
            driver = None
            driver_path = self.ut.get_driver_path('/dependencies/dir_geckodriver/geckodriver')
            self.log.log_info("Setting path of geckodriver")
            self.log.log_info("Executable path for geckodriver is set")
            if not geckoArgs:
                driver = webdriver.Firefox(executable_path=driver_path)
            else:
                while '' in geckoArgs:
                    geckoArgs.remove()
                for val in geckoArgs:
                    firefoxOptions.add_argument(val)
                driver = webdriver.Firefox(
                            executable_path=driver_path,
                            firefox_options=firefoxOptions
                        )
            self.log.log_info("Executable path for geckodriver is set")
            return driver
        except WebDriverException as e:
            self.log.log_error("There is an exception in the Web Driver configuration")
            self.log.log_error(e)