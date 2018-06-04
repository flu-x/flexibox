from selenium import webdriver
from browserium.utility.utility import Utility
from selenium.webdriver.opera.options import Options
from selenium.common.exceptions import WebDriverException
from browserium.utility.os_type import OS_type

class OperaDriverObject(Utility, OS_type):
    # Set geckodriver path
    # Pass the option 'headless' if it is needed to run gecko in headless
    # configuration
    def set_operadriver_object(self):
        try:
            os_type = self.os_name()
            driver = None
            if os_type == "macos":
                driver_path = self.get_driver_path('/dependencies/dir_operadriver/operadriver_mac64/operadriver')
                self.set_executable_permission(driver_path)
                self.log_message("INFO","setting path of operadriver")
                driver = webdriver.Opera(executable_path=driver_path)
                self.log_message("INFO","Path for opera binary is set")
            if os_type == "linux":
                driver_path = self.get_driver_path('/dependencies/dir_operadriver/operadriver_linux64/operadriver')
                self.set_executable_permission(driver_path)
                self.log_message("INFO","setting path of operadriver")
                driver = webdriver.Opera(executable_path=driver_path)
                self.log_message("INFO","Path for opera binary is set")
            return driver
        except WebDriverException as e:
            self.log_message("ERROR","There is an exception in the Web Driver configuration")
            print e