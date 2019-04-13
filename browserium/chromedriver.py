from browserium.utility.utility import Utility
from browserium.utility.os_type import OS_type
from browserium.utility.logger import Logger
import requests
import os

class Chromedriver(object):

    def __init__(self):
        self.ut = Utility()
        self.ot = OS_type()
        self.log = Logger()

    # Get the required chromedriver informations from the downloader_config.ini
    # Use the config_reader function from the Utility class to read the required configuration
    def chromedriver_objects(self):
        config_dict = {}
        config_parser = self.ut.config_reader()
        driver_type = config_parser.get('ChromeDriver','name')
        api_url = config_parser.get('ChromeDriver','url')
        latest_release = config_parser.get('ChromeDriver','latest_browser_driver')
        arch = config_parser.get('ChromeDriver','arch_type')

        config_dict = {
            'driver_type':driver_type,
            'api_url':api_url,
            'latest_release':latest_release,
            'arch':arch
        }

        return config_dict

    # build the required download url based on the information gathered using the
    # chromedriver_objects function
    def url_builder(self, os_extension):
        data = self.chromedriver_objects()
        LATEST_RELEASE = requests.get(data['latest_release'])
        url_builder = data['api_url']+LATEST_RELEASE.text+'/'+data['driver_type']+os_extension+data['arch']+'.zip'
        return url_builder

    # Download the required chromedriver binary based on the operating system type
    def evaluate_on_environment(self, os_name, arch_type):
        dir_path = self.ut.get_driver_path("/dependencies/dir_chromedriver")
        if os_name == 'macos' and arch_type == '64':
            self.ut.log_message("INFO","Environment: "+os_name)
            self.ut.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_mac = self.url_builder('_mac')
            self.ut.log_message("INFO","Downloading the required binary for chromedriver")
            self.ut.driver_downloader(url_builder_mac, dir_path)
            self.ut.log_message("INFO", "Download completed")
            self.ut.unzip_file('dir_chromedriver/')
            self.ut.log_message("INFO","Unarchiving contents completed")
        if os_name == 'linux' and arch_type == '64':
            self.ut.log_message("INFO","Environment: "+os_name)
            self.ut.log_message("INFO","Architecture Type: "+arch_type)
            url_builder_linux = self.url_builder('_linux')
            self.ut.log_message("INFO","Downloading the required binary for chromedriver")
            self.ut.driver_downloader(url_builder_linux, dir_path)
            self.ut.log_message("INFO", "Download completed")
            self.ut.unzip_file('dir_chromedriver/')
            self.ut.log_message("INFO","Unarchiving contents completed")

    # Create a required directory separately for Chrome and called the evaluate_on_environment
    # function to download the required binary
    def download_driver(self):
        dir_path = self.ut.get_driver_path("/dependencies/dir_chromedriver")
        if os.path.exists(dir_path):
            self.ut.log_message("INFO","chrome driver is already present. To update chromedriver please run `browserium update --driver=chromedriver`")
        else:
            os.makedirs(dir_path)
            os_name = self.ot.os_name()
            arch_type = str(self.ot.os_architecture())
            self.evaluate_on_environment(os_name, arch_type)

    # Update the required chromedriver based on the operating system type
    def update_driver(self):
        self.ut.check_directory_content("/dependencies/dir_chromedriver/chromedriver")
        self.ut.log_message("INFO","Deleting directory contents")
        self.ut.delete_dir_contents('dir_chromedriver/')
        os_name = self.ot.os_name()
        arch_type = str(self.ot.os_architecture())
        self.evaluate_on_environment(os_name, arch_type)
        self.ut.log_message("INFO","chromedriver updated")