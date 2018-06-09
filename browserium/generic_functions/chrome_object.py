from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from browserium.utility.utility import Utility
from browserium.utility.os_type import OS_type

class ChromeDriverObject(Utility, OS_type):
    # Set chromedriver path
    # Pass the option 'headless' if it is needed to run chrome in headless
    # configuration
    def set_chromedriver_object(self, args=""):
        os_name = self.os_name()
        try:
            driver = None
            driver_path = self.get_driver_path('/dependencies/dir_chromedriver/chromedriver')
            self.set_executable_permission(driver_path)
            self.log_message("INFO","setting executable permission to the chrome binary")
            if not '--headless' in args:
                self.log_message("INFO","setting path of chromedriver")
                driver = webdriver.Chrome(executable_path=driver_path)
                self.log_message("INFO","Path for chrome binary is set")
            else:
                self.log_message("INFO","setting chrome into headless mode")
                chromeOptions = webdriver.ChromeOptions()
                chromeOptions.add_argument(args)
                self.log_message("INFO","setting path of chromedriver")
                driver = webdriver.Chrome(
                    executable_path=driver_path, 
                    chrome_options=chromeOptions                        
                )
                self.log_message("INFO","Path for chrome binary is set")
            if "linux" in os_name:
                if not '--headless' in args:
                    chromeOptions = webdriver.ChromeOptions()
                    chromeOptions.add_argument(args)
                    chromeOptions.add_experimental_option("useAutomationExtension", False)
                    self.log_message("INFO","setting path of chromedriver")
                    driver = webdriver.Chrome(
                        executable_path=driver_path,
                        chrome_options=chromeOptions                        
                    )
                    self.log_message("INFO","Path for chrome binary is set")
                else:
                    self.log_message("INFO","setting chrome into headless mode")
                    chromeOptions = webdriver.ChromeOptions()
                    chromeOptions.add_argument(args)
                    chromeOptions.add_argument("--disable-dev-shm-usage")
                    chromeOptions.add_argument("--no-sandbox")
                    self.log_message("INFO","setting path of chromedriver")
                    driver = webdriver.Chrome(
                        executable_path=driver_path, 
                        chrome_options=chromeOptions                        
                    )
                    self.log_message("INFO","Path for chrome binary is set")
            return driver
        except WebDriverException as e:
            self.log_message("ERROR","There is an exception in the Web Driver configuration")
            print e