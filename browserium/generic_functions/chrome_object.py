from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from browserium.utility.utility import Utility

class ChromeDriverObject():

    def __init__(self):
        self.ut = Utility()

    # Set chromedriver path
    # Pass the option 'headless' if it is needed to run chrome in headless
    # configuration
    def set_chromedriver_object(self, chromeArgs=[]):
        try:
            chromeOptions = webdriver.ChromeOptions()
            driver = None
            driver_path = self.ut.get_driver_path('/dependencies/dir_chromedriver/chromedriver')
            self.ut.set_executable_permission(driver_path)
            self.ut.log_message("INFO","setting executable permission to the chrome binary")
            self.ut.log_message("INFO","setting path of chromedriver")
            if not chromeArgs:
                driver = webdriver.Chrome(executable_path=driver_path)
            else:
                while '' in chromeArgs:
                    chromeArgs.remove('')
                for val in chromeArgs:
                    chromeOptions.add_argument(val)
                driver = webdriver.Chrome(
                            executable_path=driver_path,
                            chrome_options=chromeOptions
                        )
            self.ut.log_message("INFO","Path for chrome binary is set")
            return driver
        except WebDriverException as e:
            self.ut.log_message("ERROR","There is an exception in the Web Driver configuration")
            print e