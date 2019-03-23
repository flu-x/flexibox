# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Utility is to consist of the generic functions that
# can be used across all the functionalities that would be developed in this project

from configparser import SafeConfigParser
from time import sleep
from zipfile import ZipFile
from datetime import datetime
from browserium.utility.logger import Logger
import wget
import requests
import os
import stat
import sys
import shutil
import tarfile
import json

class Utility(object):

    def __init__(self):
        self.log = Logger()

    # This method would get the required path for the directory or a file.
    # This would generate the absolute path to the required directory and the file
    def get_path(self, path_param):
        try:
            requiredPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return requiredPath
        except IOError as e:
            self.log.log_error("Required Directory / File not found")
            self.log.log_error(e)

    # This method would get the required configuration from the config.ini file
    # and ould return the parser object which can be utilised as required.
    def config_reader(self):
        parser = SafeConfigParser()
        parser.read(self.get_path('../configurations/downloader_config.ini'))
        return parser

    # This method would download the required binaries and packages required
    # for the respective browser
    def driver_downloader(self, api_url, dir_path):
        try:
            request_api = requests.get(api_url, stream=True)
            if request_api.status_code == 200:
                wget.download(api_url, out=dir_path)
            else:
                request_api.raise_for_status()
        except requests.exceptions.Timeout:
            self.log.log_error("Request time out encountered")
        except requests.exceptions.TooManyRedirects:
            self.log.log_error("Too many redirects encountered")
        except requests.exceptions.HTTPError as e:
            self.log.log_error(e)
            sys.exit(1)

    # This method would parse the required json object and would return back
    # the required JSON from where we can extract the required information.
    def api_parser(self, api_url):
        try:
            response=None
            request_api = requests.get(api_url)
            if request_api.status_code == 200:
                request = requests.get(api_url)
                response = request.json()
                return response
            else:
                request.raise_for_status()
        except requests.exceptions.Timeout:
            self.log.log_error("Request time out encountered")
        except requests.exceptions.TooManyRedirects:
            self.log.log_error("Too many redirects encountered")
        except requests.exceptions.HTTPError:
            self.log.log_error("HTTP error encountered")
            sys.exit(1)

    # Get the required download URLs from the API data based on the operating system type
    def get_api_data(self, api_url):
        linux = None
        mac = None
        env = {}
        api_response = self.api_parser(api_url)
        for ent in api_response['assets']:
            if "_linux64" in ent['browser_download_url']:
                linux = ent['browser_download_url']
            if "_mac64" in ent['browser_download_url']:
                mac = ent['browser_download_url']
            if "linux32.tar.gz" in ent['browser_download_url']:
                linux = ent['browser_download_url']
            if "linux64.tar.gz" in ent['browser_download_url']:
                linux = ent['browser_download_url']
            if "macos.tar.gz" in ent['browser_download_url']:
                mac = ent['browser_download_url']

        env = {
            "linux": linux,
            "mac": mac
        }
        return env

    # Unzip the required .zip package based on the path of the zip file.
    def unzip_file(self, dir_path):
        try:
            zipFile_path = Utility.get_driver_path('/dependencies/'+dir_path)
            file_info = os.listdir(zipFile_path)
            sleep(2)
            for i in file_info:
                with ZipFile(zipFile_path + i, 'r') as zipfile:
                    zipfile.extractall(zipFile_path)
                    zipfile.close()
        except OSError:
            self.log.log_error("File / Directory " + dir_path + "not found")

    # Unzip the required .gzip package based on the path of the gzip file.
    def untar_file(self, dir_path):
        try:
            tarFile_path = Utility.get_driver_path('/dependencies/'+dir_path)
            file_info = os.listdir(tarFile_path)
            sleep(2)
            for fname in file_info:
                tar = tarfile.open(tarFile_path+fname, "r:gz")
                tar.extractall(tarFile_path)
                tar.close()
        except OSError:
            self.log.log_error("File / Directory " + dir_path + "not found")

    # Rename the required directory
    def rename_dir(self, dir_path):
        try:
            dir_path = Utility.get_driver_path('/dependencies/'+dir_path)
            file_info = os.listdir(dir_path)
            os.rename(dir_path+file_info[1],dir_path+'phantomjsdriver')
        except OSError:
            self.log.log_error("File / Directory " + dir_path + "not found")

    # Delete the contents of the directory when updating a package
    def delete_dir_contents(self, dir_content_directory):
        dep_tree = Utility.get_driver_path('/dependencies/'+dir_content_directory)
        try:
            for item in os.listdir(dep_tree):
                if item.endswith(".zip"):
                    os.remove(dep_tree+item)
                elif os.path.isdir(dep_tree+item):
                    shutil.rmtree(dep_tree+item)
                else:
                    os.remove(dep_tree+item)
        except OSError:
            self.log.log_error("File / Directory " + dir_content_directory + "not found")

    # Checkpoint to verify driver is there in the directory before updating the driver binary
    def check_directory_content(self, file_dir_path):
        if not os.path.exists(Utility.get_driver_path(file_dir_path)):
            self.log.log_warning("You cannot update the respective driver binary first without downloading it")
            sys.exit(0)
        else:
            pass

    # Get the current time stamp
    @staticmethod
    def get_current_time_stamp():
        curr_timestamp = str(datetime.now())
        return curr_timestamp

    # Print the required message
    @staticmethod
    def log_message(log_type, log_message):
        time_stamp = Utility.get_current_time_stamp()
        log_message = "["+time_stamp+"]: "+"["+log_type+"] - "+log_message
        print(log_message)

    # Get the path for the drivers
    @staticmethod
    def get_driver_path(path):
        driver_path = "/usr/local/bin"+path
        return driver_path

    # Set executable permission for drivers
    @staticmethod
    def set_executable_permission(driver_path):
        st = os.stat(driver_path)
        os.chmod(driver_path, st.st_mode | stat.S_IEXEC)

    # Delete driver executables from /usr/local/bin
    def delete_driver_history(self):
        rel_dir_path = Utility.get_driver_path("/dependencies")
        if not os.path.exists(rel_dir_path):
            self.log.log_error("Driver directory does not exist")
        else:
            shutil.rmtree(rel_dir_path, ignore_errors=True)
            self.log.log_info("Deleted driver directory from /usr/local/bin")

    # return json data
    @staticmethod
    def json_file_reader(file_path):
        with open(file_path) as data_file:
            json_data = json.loads(data_file)
            return json_data