import os
import unittest

import requests
import wget
from utility import Utility_object

from flexibox.core.logger import Logger


class TestChrome(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.utility = Utility_object()
        self.log = Logger()

    def parseJSONChrome(self):
        dict_data = {}
        jsonData = self.utility.json_file_reader()
        for item in jsonData['assets']:
            dict_data = {
                "url": item['chromedriver']['url'],
                "release_version": item['chromedriver']['release_version'],
                "mac_v_64": item['chromedriver']['mac_v_64'],
                "linux_v_64": item['chromedriver']['linux_v_64']
            }
        return dict_data

    def testChromeDriverMac(self):
        _data = self.parseJSONChrome()
        _releaseVersionAPI = _data.get('release_version')
        _releaseVersion = ""
        response = requests.get(_releaseVersionAPI)
        try:
            if response.status_code == 200:
                _releaseVersion = response.text
        except requests.exceptions.Timeout:
            self.log.log_error("Request time out")
        except requests.exceptions.TooManyRedirects:
            self.log.log_error("Too many redirects")
        except requests.exceptions.RequestException as e:
            self.log.log_error(e)

        _url = _data.get('url')

        _mac_bin = _data.get('mac_v_64')

        # API url
        _apiURLBuilder = _url + _releaseVersion + "/" + _mac_bin

        # Download file
        try:
            _url = requests.get(_apiURLBuilder)
            if _url.status_code == 200:
                wget.download(_apiURLBuilder)
                self.log.log_info("Binary for chromedriver downloaded for macOS")
        except requests.exceptions.Timeout:
            self.log.log_error("Request time out")
        except requests.exceptions.TooManyRedirects:
            self.log.log_error("Too many redirects")
        except requests.exceptions.RequestException as e:
            self.log.log_error(e)

        # Assert for file exists
        self.assertTrue(os.path.exists('chromedriver_mac64.zip'))
        self.log.log_info("Required path for binary exist")

        # Delete file
        self.utility.delete_file("chromedriver_mac64.zip")
        self.log.log_info("Downloaded binaries deleted")

    def testChromeDriverLinux(self):
        _data = self.parseJSONChrome()
        _releaseVersionAPI = _data.get('release_version')
        _releaseVersion = ""

        response = requests.get(_releaseVersionAPI)
        try:
            if response.status_code == 200:
                _releaseVersion = response.text
        except requests.exceptions.Timeout:
            self.log.log_error("Request time out")
        except requests.exceptions.TooManyRedirects:
            self.log.log_error("Too many redirects")
        except requests.exceptions.RequestException as e:
            self.log.log_error(e)

        _url = _data.get('url')
        _linux_bin = _data.get('linux_v_64')

        # API url
        _apiURLBuilder = _url + _releaseVersion + "/" + _linux_bin

        # Download file
        try:
            _url = requests.get(_apiURLBuilder)
            if _url.status_code == 200:
                wget.download(_apiURLBuilder)
                self.log.log_info("Binary for chromedriver downloaded for Linux")
        except requests.exceptions.Timeout:
            self.log.log_error("Request time out")
        except requests.exceptions.TooManyRedirects:
            self.log.log_error("Too many redirects")
        except requests.exceptions.RequestException as e:
            self.log.log_error(e)

        # Assert for file exists
        self.assertTrue(os.path.exists('chromedriver_linux64.zip'))
        self.log.log_info("Required path for binary exist")

        # Delete file
        self.utility.delete_file("chromedriver_linux64.zip")
        self.log.log_info("Deleted respective binary")
