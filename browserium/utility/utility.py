# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Utility is to consist of the generic functions that
# can be used across all the functionalities that would be developed in this project

from ConfigParser import SafeConfigParser
from time import sleep
from zipfile import ZipFile
from datetime import datetime
import wget
import requests
import os
import stat
import sys
import shutil
import tarfile
import argparse
import json
class Utility():
    # This method would get the required path for the directory or a file.
    # This would generate the absolute path to the required directory and the file
    @staticmethod
    def get_path(path_param):
        try:
            requiredPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return requiredPath
        except IOError as e:
            Utility.log_message("ERROR", "Required Directory / File not found")
            print e

    # This method would get the required configuration from the config.ini file
    # and ould return the parser object which can be utilised as required.
    @staticmethod
    def config_reader():
        parser = SafeConfigParser()
        parser.read(Utility.get_path('../configurations/downloader_config.ini'))
        return parser

    # This method would download the required binaries and packages required
    # for the respective browser
    @staticmethod
    def driver_downloader(api_url, dir):
        try:
            request_api = requests.get(api_url, stream=True)
            if request_api.status_code == 200:
                wget.download(api_url, out=dir)
            else:
                request_api.raise_for_status()
        except requests.exceptions.Timeout:
            Utility.log_message("ERROR","Request time out encountered")
        except requests.exceptions.TooManyRedirects:
            Utility.log_message("ERROR","Too many redirects encountered")
        except requests.exceptions.HTTPError as e:
            print e
            sys.exit(1)

    # This method would parse the required json object and would return back
    # the required JSON from where we can extract the required information.
    @staticmethod
    def api_parser(api_url):
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
            Utility.log_message("ERROR","Request time out encountered")
        except requests.exceptions.TooManyRedirects:
            Utility.log_message("ERROR","Too many redirects encountered")
        except requests.exceptions.HTTPError:
            Utility.log_message("ERROR","Too many redirects encountered")
            sys.exit(1)

    # Get the required download URLs from the API data based on the operating system type
    @staticmethod
    def get_api_data(api_url):
        linux = None
        mac = None
        env = {}
        api_response = Utility.api_parser(api_url)
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
    @staticmethod
    def unzip_file(dir_path):
        try:
            zipFile_path = Utility.get_driver_path('/dependencies/'+dir_path)
            file_info = os.listdir(zipFile_path)
            sleep(2)
            for i in file_info:
                with ZipFile(zipFile_path + i, 'r') as zip:
                    zip.extractall(zipFile_path)
                    zip.close()
        except OSError:
            Utility.log_message("ERROR","File / Directory " + dir_path + "not found")

    # Unzip the required .gzip package based on the path of the gzip file.
    @staticmethod
    def untar_file(dir_path):
        try:
            tarFile_path = Utility.get_driver_path('/dependencies/'+dir_path)
            file_info = os.listdir(tarFile_path)
            sleep(2)
            for fname in file_info:
                tar = tarfile.open(tarFile_path+fname, "r:gz")
                tar.extractall(tarFile_path)
                tar.close()
        except OSError:
            Utility.log_message("ERROR","File / Directory " + dir_path + "not found")

    # Rename the required directory
    @staticmethod
    def rename_dir(dir_path):
        try:
            dir_path = Utility.get_driver_path('/dependencies/'+dir_path)
            file_info = os.listdir(dir_path)
            os.rename(dir_path+file_info[1],dir_path+'phantomjsdriver')
        except OSError:
            Utility.log_message("ERROR","File / Directory " + dir_path + "not found")

    # Delete the contents of the directory when updating a package
    @staticmethod
    def delete_dir_contents(dir_content_directory):
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
            Utility.log_message("ERROR","File / Directory " + dir_content_directory + "not found")

    # Checkpoint to verify driver is there in the directory before updating the driver binary
    @staticmethod
    def check_directory_content(file_dir_path):
        if not os.path.exists(Utility.get_driver_path(file_dir_path)):
            Utility.log_message("INFO","You cannot update the respective driver binary first without downloading it")
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
        print log_message

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
    @staticmethod
    def delete_driver_history():
        rel_dir_path = Utility.get_driver_path("/dependencies")
        if not os.path.exists(rel_dir_path):
            Utility.log_message("INFO", "Driver directory does not exist")
        else:
            shutil.rmtree(rel_dir_path, ignore_errors=True)
            Utility.log_message("INFO", "Deleted driver directory from /usr/local/bin")

    # return json data
    @staticmethod
    def json_file_reader(file_path):
        with open(file_path) as data_file:
            json_data = json.loads(data_file)
            return json_data