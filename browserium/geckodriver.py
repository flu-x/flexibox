from utility.utility import Utility
from utility.os_type import OS_type
from selenium import webdriver
import requests
import os
import shutil
class Geckodriver(Utility, OS_type):
    # Get the required chromedriver informations from the downloader_config.ini
    # Use the config_reader function from the Utility class to read the required configuration
    def geckodriver_object(self):
        config_parser = self.config_reader()
        api_url = config_parser.get('GeckoDriver','latest_browser_driver')
        return api_url

    # build the required download url based on the information gathered using the
    # geckodriver_objects function
    def parse_geckodriver_api(self):
        api_url = self.geckodriver_object()
        browser_api_url = self.get_api_data(api_url)
        return browser_api_url

    # Download the required geckodriver binary based on the operating system type
    def evaluate_on_environment(self, os_name, arch_type):
        dir_path = self.get_driver_path('/dependencies/dir_geckodriver')
        if os_name == 'macos' and arch_type == '64':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_mac = self.parse_geckodriver_api()
            self.log_message("INFO","Downloading the required binary for geckodriver")
            self.driver_downloader(url_builder_mac['mac'], dir_path)
            print "\n"
            self.log_message("INFO", "Download completed")
            self.untar_file('dir_geckodriver/')
            self.log_message("INFO","Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '64':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_linux = self.parse_geckodriver_api()
            self.log_message("INFO","Downloading the required binary for geckodriver")
            self.driver_downloader(url_builder_linux['linux'], dir_path)
            print "\n"
            self.log_message("INFO", "Download completed")
            self.untar_file('dir_operadriver/')
            self.log_message("INFO","Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '32':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_linux = self.parse_geckodriver_api()
            self.log_message("INFO","Downloading the required binary for geckodriver")
            self.driver_downloader(url_builder_linux['linux'], dir_path)
            print "\n"
            self.log_message("INFO", "Download completed")
            self.untar_file('dir_operadriver/')
            self.log_message("INFO","Unarchiving contents completed")

    # Create a required directory separately for gecko and called the evaluate_on_environment
    # function to download the required binary
    def download_driver(self):
        dir_path = self.get_driver_path('/dependencies/dir_geckodriver')
        if os.path.exists(dir_path):
            self.log_message("INFO","gecko driver is already present. To update gecko driver please run `browserium update --driver=geckodriver`")
        else:
            os.makedirs(dir_path)
            os_name = self.os_name()
            arch_type = str(self.os_architecture())
            self.evaluate_on_environment(os_name, arch_type)

    # Update the required geckodriver based on the operating system type
    def update_driver(self):
        self.log_message("INFO","Deleting directory contents")
        self.check_directory_content("/dependencies/dir_geckodriver/geckodriver")
        self.delete_dir_contents('dir_geckodriver/')
        os_name = self.os_name()
        arch_type = str(self.os_architecture())
        self.evaluate_on_environment(os_name, arch_type)
        self.log_message("INFO","geckodriver updated")