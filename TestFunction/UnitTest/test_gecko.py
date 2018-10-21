from utility import Utility_object
import unittest
import requests
import wget
import os

class TestGecko(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.utility=Utility_object()

    def parseJSONGecko(self):
        jsonData = self.utility.json_file_reader()
        apiURL = ""
        for item in jsonData['assets']:
            apiURL = item['geckodriver']['apiURL']
        return apiURL

    def parseJSONResponse(self):
        linux_downloadURL_32 = None
        linux_downloadURL_64 = None
        mac_downloadURL = None
        linux_tagName_32 = None
        linux_tagName_64 = None
        mac_tagName = None
        env = {}

        _response = requests.get(self.parseJSONGecko())
        if _response.status_code == 200:
            data = _response.json()
            for ent in data['assets']:
                if "linux32.tar.gz" in ent['browser_download_url']:
                    linux_downloadURL_32 = ent['browser_download_url']
                    linux_tagName_32 = ent['name']
                if "linux64.tar.gz" in ent['browser_download_url']:
                    linux_downloadURL_64 = ent['browser_download_url']
                    linux_tagName_64 = ent['name']
                if "macos.tar.gz" in ent['browser_download_url']:
                    mac_downloadURL = ent['browser_download_url']
                    mac_tagName = ent['name']

        env = {
            "linux_downloadURL_32": linux_downloadURL_32,
            "linux_tagName_32": linux_tagName_32,
            "linux_downloadURL_64": linux_downloadURL_64,
            "linux_tagName_64": linux_tagName_64,
            "mac_downloadURL": mac_downloadURL,
            "mac_tagName": mac_tagName
        }

        return env

    def testGeckoDriverMac(self):
        _data = self.parseJSONResponse()
        _geckoBinMacDownloadURL = _data.get('mac_downloadURL')
        _geckoBinMacTagName = _data.get('mac_tagName')

        #Download driver
        wget.download(_geckoBinMacDownloadURL)

        print "\n"
        self.utility.log_message("INFO", "Binary for geckodriver downloaded for macOS")

        #Assert for file exists
        self.assertTrue(os.path.exists(_geckoBinMacTagName))

        #Delete file
        self.utility.delete_file(_geckoBinMacTagName)

    def testGeckoDriverLinux32(self):
        _data = self.parseJSONResponse()
        _geckoBinLinux32DownloadURL = _data.get('linux_downloadURL_32').strip()
        _geckoBinLinux32TagName = _data.get('linux_tagName_32').strip()

        #Download driver
        wget.download(_geckoBinLinux32DownloadURL)

        print "\n"
        self.utility.log_message("INFO", "Binary for geckodriver downloaded for Linux 32 bit")

        #Assert for file exists
        self.assertTrue(os.path.exists(_geckoBinLinux32TagName))

        #Delete file
        self.utility.delete_file(_geckoBinLinux32TagName)

    def testGeckoDriverLinux64(self):
        _data = self.parseJSONResponse()
        _geckoBinLinux64DownloadURL = _data.get('linux_downloadURL_64').strip()
        _geckoBinLinux64TagName = _data.get('linux_tagName_64').strip()

        #Download driver
        wget.download(_geckoBinLinux64DownloadURL)

        print "\n"
        self.utility.log_message("INFO", "Binary for geckodriver downloaded for Linux 64 bit")

        #Assert for file exists
        self.assertTrue(os.path.exists(_geckoBinLinux64TagName))

        #Delete file
        self.utility.delete_file(_geckoBinLinux64TagName)