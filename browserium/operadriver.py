from browserium.utility.utility import Utility
from browserium.utility.os_type import OS_type
from browserium.utility.logger import Logger
import os

class Operadriver(object):

    def __init__(self):
        self.ut = Utility()
        self.ot = OS_type()
        self.log = Logger()

    # Get the required chromedriver informations from the downloader_config.ini
    # Use the config_reader function from the Utility class to read the required configuration
    def operadriver_object(self):
        config_parser = self.ut.config_reader()
        api_url = config_parser.get('OperaDriver','latest_browser_driver')
        return api_url

    # build the required download url based on the information gathered using the
    # chromedriver_objects function
    def parse_operadriver_api(self):
        api_url = self.operadriver_object()
        browser_api_url = self.ut.get_api_data(api_url)
        return browser_api_url

    # Download the required chromedriver binary based on the operating system type
    def evaluate_on_environment(self, os_name, arch_type):
        dir_path = self.ut.get_driver_path('/dependencies/dir_operadriver')
        if os_name == 'macos' and arch_type == '64':
            self.log.log_info("Environment: "+os_name)
            self.log.log_info("Architecture Type: "+arch_type)
            url_builder_mac = self.parse_operadriver_api()
            self.log.log_info("Downloading the required binary for operadriver")
            self.ut.driver_downloader(url_builder_mac['mac'], dir_path)
            self.log.log_info("Download completed")
            self.ut.unzip_file('dir_operadriver/')
            self.log.log_info("Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '64':
            self.log.log_info("Environment: "+os_name)
            self.log.log_info("Architecture Type: "+arch_type)
            url_builder_linux = self.parse_operadriver_api()
            self.log.log_info("Downloading the required binary for operadriver")
            self.ut.driver_downloader(url_builder_linux['linux'], dir_path)
            self.log.log_info("Download completed")
            self.ut.unzip_file('dir_operadriver/')
            self.log.log_info("Unarchiving contents completed")

    # Create a required directory separately for Opera and called the evaluate_on_environment
    # function to download the required binary
    def download_driver(self):
        dir_path = self.ut.get_driver_path('/dependencies/dir_operadriver')
        if os.path.exists(dir_path):
             self.log.log_info("Opera driver is already present. To update operadriver please run `browserium update --driver=operadriver`")
        else:
            os.makedirs(dir_path)
            os_name = self.ot.os_name()
            arch_type = str(self.ot.os_architecture())
            self.evaluate_on_environment(os_name, arch_type)

    def update_driver(self):
        self.log.log_info("Deleting directory contents")
        self.ut.check_directory_content("/dependencies/dir_operadriver")
        self.ut.delete_dir_contents('dir_operadriver/')
        os_name = self.ot.os_name()
        arch_type = str(self.ot.os_architecture())
        self.evaluate_on_environment(os_name, arch_type)
        self.log.log_info("Operadriver updated")