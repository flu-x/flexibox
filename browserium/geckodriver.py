from browserium.utility.utility import Utility
from browserium.utility.os_type import OS_type
from browserium.utility.logger import Logger
import os

class Geckodriver(object):

    def __init__(self):
        self.ut = Utility()
        self.ot = OS_type()
        self.log = Logger()
    # Get the required chromedriver informations from the downloader_config.ini
    # Use the config_reader function from the Utility class to read the required configuration
    def geckodriver_object(self):
        config_parser = self.ut.config_reader()
        api_url = config_parser.get('GeckoDriver','latest_browser_driver')
        return api_url

    # build the required download url based on the information gathered using the
    # geckodriver_objects function
    def parse_geckodriver_api(self):
        api_url = self.geckodriver_object()
        browser_api_url = self.ut.get_api_data(api_url)
        return browser_api_url

    # Download the required geckodriver binary based on the operating system type
    def evaluate_on_environment(self, os_name, arch_type):
        dir_path = self.ut.get_driver_path('/dependencies/dir_geckodriver')
        if os_name == 'macos' and arch_type == '64':
            self.log.log_info("Environment: "+os_name)
            self.log.log_info("Architecture Type: "+arch_type)
            url_builder_mac = self.parse_geckodriver_api()
            self.log.log_info("Downloading the required binary for geckodriver")
            self.ut.driver_downloader(url_builder_mac['mac'], dir_path)
            self.log.log_info("Download completed")
            self.ut.untar_file('dir_geckodriver/')
            self.log.log_info("Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '64':
            self.log.log_info("Environment: "+os_name)
            self.log.log_info("Architecture Type: "+arch_type)
            url_builder_linux = self.parse_geckodriver_api()
            self.log.log_info("Downloading the required binary for geckodriver")
            self.ut.driver_downloader(url_builder_linux['linux'], dir_path)
            self.log.log_info("Download completed")
            self.ut.untar_file('dir_geckodriver/')
            self.log.log_info("Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '32':
            self.log.log_info("Environment: "+os_name)
            self.log.log_info("Architecture Type: "+arch_type)
            url_builder_linux = self.parse_geckodriver_api()
            self.log.log_info("Downloading the required binary for geckodriver")
            self.ut.driver_downloader(url_builder_linux['linux'], dir_path)
            self.log.log_info("Download completed")
            self.ut.untar_file('dir_geckodriver/')
            self.log.log_info("Unarchiving contents completed")

    # Create a required directory separately for gecko and called the evaluate_on_environment
    # function to download the required binary
    def download_driver(self):
        dir_path = self.ut.get_driver_path('/dependencies/dir_geckodriver')
        if os.path.exists(dir_path):
            self.log.log_info("gecko driver is already present. To update gecko driver please run `browserium update --driver=geckodriver`")
        else:
            os.makedirs(dir_path)
            os_name = self.ot.os_name()
            arch_type = str(self.ot.os_architecture())
            self.evaluate_on_environment(os_name, arch_type)

    # Update the required geckodriver based on the operating system type
    def update_driver(self):
        self.log.log_info("Deleting directory contents")
        self.ut.check_directory_content("/dependencies/dir_geckodriver/geckodriver")
        self.ut.delete_dir_contents('dir_geckodriver/')
        os_name = self.ot.os_name()
        arch_type = str(self.ot.os_architecture())
        self.evaluate_on_environment(os_name, arch_type)
        self.log.log_info("geckodriver updated")