from utility import Utility_object
import unittest
import requests
import json
import wget

class TestGecko(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.utility=Utility_object()

    def parse_json(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            return data['browser_download_url']

    def parseJSONGecko(self):
        dict_data = {}
        jsonData = self.utility.json_file_reader()
        for item in jsonData['assets']:
            dict_data = {
                "macos" : item['geckodriver']['macos_v'],
                "linux_64" : item['geckodriver']['linux_v_64'],
                "linux_32" : item['geckodriver']['linux_v_32']
            }
        return dict_data

    def testGeckoDriverMac(self):
        driverAPI = self.parseJSONGecko()
        data = driverAPI.get('macos')
        download_url = self.parse_json(data)

        _response = requests.get(download_url)
        if _response.status_code == 200:
            wget.download(download_url)

        self.utility.log_message("INFO", "Binary for operadriver downloaded for macOS")

    def testGeckoDriverLinux64(self):
        driverAPI = self.parseJSONGecko()
        data = driverAPI.get('linux_64')
        download_url = self.parse_json(data)

        _response = requests.get(download_url)
        if _response.status_code == 200:
            wget.download(download_url)

        self.utility.log_message("INFO", "Binary for operadriver downloaded for LINUX")

    def testGeckoDriverLinux32(self):
        driverAPI = self.parseJSONGecko()
        data = driverAPI.get('linux_32')
        download_url = self.parse_json(data)

        _response = requests.get(download_url)
        if _response.status_code == 200:
            wget.download(download_url)

        self.utility.log_message("INFO", "Binary for operadriver downloaded for LINUX")