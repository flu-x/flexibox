from utility.utility import Utility_object
import unittest
import requests
import json
import wget

class TestChrome(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.utility = Utility_object()

    def parse_json(self, api):
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            return data['browser_download_url']

    def parseJSONChrome(self):
        dict_data = {}
        jsonData = self.utility.json_file_reader()
        for item in jsonData['assets']:
            dict_data = {
                "url" : item['chromedriver']['url'],
                "release_version" : item['chromedriver']['release_version'],
                "mac_v_64" : item['chromedriver']['mac_v_64'],
                "linux_v_64" : item['chromedriver']['linux_v_64']
            }
        return dict_data

    def testChromeDriverMac(self):
        _data = self.parseJSONChrome()
        _releaseVersionAPI = _data.get('release_version')
        _releaseVersion = ""

        response = requests.get(_releaseVersionAPI)
        if response.status_code == 200:
            _releaseVersion = str(response.json())

        _url = _data.get('url')
        print _url
        _mac_bin = _data.get('mac_v_64')

        _apiURLBuilder = _url+_releaseVersion+"/"+_mac_bin

        _url = requests.get(_apiURLBuilder)
        if _url.status_code == 200:
            wget.download(_apiURLBuilder)

    def testChromeDriverLinux(self):
        _data = self.parseJSONChrome()
        _releaseVersionAPI = _data.get('release_version')
        _releaseVersion = ""

        response = requests.get(_releaseVersionAPI)
        if response.status_code == 200:
            _releaseVersion = str(response.json())

        _url = _data.get('url')
        _linux_bin = _data.get('linux_v_64')

        _apiURLBuilder = _url+_releaseVersion+"/"+_linux_bin

        _url = requests.get(_apiURLBuilder)
        if _url.status_code == 200:
            wget.download(_apiURLBuilder)