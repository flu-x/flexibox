from utility.utility import Utility
from utility.os_type import OS_type
from selenium import webdriver
import requests
import os
import shutil

class Operadriver(Utility, OS_type):
    # Get the required chromedriver informations from the downloader_config.ini
    # Use the config_reader function from the Utility class to read the required configuration
    def operadriver_object(self):
        config_parser = self.config_reader()
        api_url = config_parser.get('OperaDriver','latest_browser_driver')
        return api_url

    # build the required download url based on the information gathered using the
    # chromedriver_objects function
    def parse_operadriver_api(self):
        api_url = self.operadriver_object()
        browser_api_url = self.get_api_data(api_url)
        return browser_api_url

    # Download the required chromedriver binary based on the operating system type
    def evaluate_on_environment(self, os_name, arch_type):
        dir_path = self.get_driver_path('/dependencies/dir_operadriver')
        if os_name == 'macos' and arch_type == '64':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_mac = self.parse_operadriver_api()
            self.log_message("INFO","Downloading the required binary for operadriver")
            self.driver_downloader(url_builder_mac['mac'], dir_path)
            print "\n"
            self.log_message("INFO", "Download completed")
            self.unzip_file('dir_operadriver/')
            self.log_message("INFO","Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '64':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_linux = self.parse_operadriver_api()
            self.log_message("INFO","Downloading the required binary for operadriver")
            self.driver_downloader(url_builder_linux['linux'], dir_path)
            print "\n"
            self.log_message("INFO", "Download completed")
            self.unzip_file('dir_operadriver/')
            self.log_message("INFO","Unarchiving contents completed")

    # Create a required directory separately for Opera and called the evaluate_on_environment
    # function to download the required binary
    def download_driver(self):
        dir_path = self.get_driver_path('/dependencies/dir_operadriver')
        if os.path.exists(dir_path):
             self.log_message("INFO","opera driver is already present. To update operadriver please run `browserium update --driver=operadriver`")
        else:
            os.makedirs(dir_path)
            os_name = self.os_name()
            arch_type = str(self.os_architecture())
            self.evaluate_on_environment(os_name, arch_type)

    def update_driver(self):
        self.log_message("INFO","Deleting directory contents")
        self.check_directory_content("/dependencies/dir_operadriver")
        self.delete_dir_contents('dir_operadriver/')
        os_name = self.os_name()
        arch_type = str(self.os_architecture())
        self.evaluate_on_environment(os_name, arch_type)
        self.log_message("INFO","operadriver updated")