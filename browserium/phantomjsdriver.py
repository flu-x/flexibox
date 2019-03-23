from utility.utility import Utility
from utility.os_type import OS_type
import os

class Phantomjs_driver(Utility, OS_type):
    # Get the required chromedriver informations from the downloader_config.ini
    # Use the config_reader function from the Utility class to read the required configuration
    def phantomjsdriver_object(self):
        config_parser = self.config_reader()
        api_url = config_parser.get('PhantomJSDriver','latest_browser_driver')
        return api_url

    # Get the required API data from the function phantomjsdriver_object
    def parse_phantomjsdriver_api(self):
        api_url = self.phantomjsdriver_object()
        api_data = self.api_parser(api_url)
        return api_data

    # Get the required download url based on the information gathered using the
    # geckodriver_objects function
    def parse_apidata(self):
        api_url = {}
        raw_json = self.parse_phantomjsdriver_api()
        api_url = {
            "zip_ball": raw_json['zipball_url'],
            "tar_ball": raw_json['tarball_url']
        }
        return api_url

    # Download the required phantomjsdriver binary based on the operating system type
    def evaluate_on_environment(self, os_name):
        download_url = self.parse_apidata()
        dir_path = self.get_driver_path('/dependencies/dir_phantomjsdriver')
        if os_name == 'macos':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Downloading the required binary for phantomjsdriver")
            self.driver_downloader(download_url['zip_ball'], dir_path)
            self.log_message("INFO", "Download completed")
            self.unzip_file('dir_phantomjsdriver/')
            self.log_message("INFO","Unarchiving contents completed")
            self.rename_dir('dir_phantomjsdriver/')
        if os_name == 'linux':
            self.log_message("INFO","Environment: "+os_name)
            self.log_message("INFO","Downloading the required binary for phantomjsdriver")
            self.driver_downloader(download_url['tar_ball'], dir_path)
            self.log_message("INFO", "Download completed")
            self.untar_file('dir_phantomjsdriver/')
            self.log_message("INFO","Unarchiving contents completed")
            self.rename_dir('dir_phantomjsdriver/')

    # Create a required directory separately for phantomjs and called the evaluate_on_environment
    # function to download the required binary
    def download_driver(self):
        dir_path = self.get_driver_path('/dependencies/dir_phantomjsdriver')
        if os.path.exists(dir_path):
            self.log_message("INFO","phantomjs driver is already present. To update phantomjsdriver please run `browserium update --driver=phantomjsdriver`")
        else:
            os.makedirs(dir_path)
            os_name = self.os_name()
            self.evaluate_on_environment(os_name)

    # Update the required phantomjsdriver based on the operating system type
    def update_driver(self):
        self.log_message("INFO","Deleting directory contents")
        self.check_directory_content('/dependencies/dir_phantomjsdriver')
        self.delete_dir_contents('dir_phantomjsdriver/')
        os_name = self.os_name()
        self.evaluate_on_environment(os_name)
        self.log_message("INFO","operadriver updated")