import os
import unittest

import requests
import wget
from requests import exceptions
from utility import Utility_object

from flexibox.core.logger import Logger


class TestOpera(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.utility = Utility_object()
        self.log = Logger()

    @classmethod
    def parse_json(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            return data['browser_download_url']

    def parseJSONOpera(self):
        dict_data = {}
        jsonData = self.utility.json_file_reader()
        for item in jsonData['assets']:
            dict_data = {"mac": item['operadriver']['mac_v_64'], "linux": item['operadriver']['linux_v_64']}
        return dict_data

    def testOperaDriverMac(self):
        driverAPI = self.parseJSONOpera()
        data = driverAPI.get('mac')
        download_url = self.parse_json(data)

        # Check response code
        _response = requests.get(download_url)
        if _response.status_code == 200:
            wget.download(download_url)
            self.log.log_info("Binary downloaded for mac")
        else:
            raise requests.exceptions.ConnectionError("Connection error")
            self.log.log_error("Connection error")

        # Assert for file exists
        self.assertTrue(os.path.exists('operadriver_mac64.zip'))
        self.log.log_info("Path for binary file exist")

        # Delete file
        self.utility.delete_file("operadriver_mac64.zip")
        self.log.log_info("Binary files deleted")

    def testOperaDriverLinux(self):
        driverAPI = self.parseJSONOpera()
        data = driverAPI.get('linux')
        download_url = self.parse_json(data)

        # Check response code
        _response = requests.get(download_url)
        if _response.status_code == 200:
            wget.download(download_url)
            self.log.log_info("Binary files downloaded")
        else:
            raise requests.exceptions.ConnectionError("Connection error")
            self.log.log_error("Connection error")

        # Assert for file exists
        self.assertTrue(os.path.exists('../TestFunction/operadriver_linux64.zip'))
        self.log.log_info("Path for binary file exist")

        # Delete file
        self.utility.delete_file("operadriver_linux64.zip")
        self.log.log_info("Binary files deleted")
