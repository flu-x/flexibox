from selenium import webdriver
from browserium.utility.utility import Utility
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

class GeckoDriverObject(object):

    def __init__(self):
        self.ut = Utility()

    # Set geckodriver path
    # Pass the option 'headless' if it is needed to run gecko in headless
    # configuration
    def set_geckodriver_object(self, geckoArgs=None):
        try:
            geckoArgs = []
            firefoxOptions = Options()
            driver = None
            driver_path = self.ut.get_driver_path('/dependencies/dir_geckodriver/geckodriver')
            self.ut.log_message("INFO","setting path of geckodriver")
            self.ut.log_message("INFO","executable path for geckodriver is set")
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
            self.ut.log_message("INFO","executable path for geckodriver is set")
            return driver
        except WebDriverException as e:
            self.ut.log_message("ERROR","There is an exception in the Web Driver configuration")
            print e