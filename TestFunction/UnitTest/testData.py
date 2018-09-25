from browserium.chromedriver import Chromedriver
from browserium.geckodriver import Geckodriver
from browserium.utility.utility import Utility
from nose.tools import assert_equals
from nose.tools import assert_true
import os
import wget
import requests

class UnittestModule(Utility, Chromedriver):

    # Apply assertion for testing equality condition
    def AssertEquals(self,actual,expected):
        assert_equals(actual, expected)

    # Apply assertion for testing boolean condition for True
    def AssertTrue(self, result):
        assert_true(result)

    # Validate response for api hits for browsers
    def response_validate(self, api_url):
        response = requests.get(api_url)
        self.AssertEquals(response,"200")

    # Validate file exists in the directory
    def file_validate(self, file):
        result = os.path.exists(file)
        self.AssertTrue(result)

    # Check api hit of chromedriver for mac
    def test_api_chromedriver_mac(self):
        api_url_mac = self.url_builder('_mac')
        print api_url_mac
        # self.response_validate(api_url_mac)
        # wget.download(api_url_mac)
        # self.file_validate("chromedriver_mac64.zip")

    # Check api hit of chromedriver for linux
    def test_api_chromedriver_linux(self):
        api_url_linux = self.url_builder("_linux")
        print api_url_linux
        # self.response_validate(api_url_linux)
        # wget.download(api_url_linux)
        # self.file_validate("chromedriver_linux64.zip")


u = UnittestModule()
u.test_api_chromedriver_mac()
u.test_api_chromedriver_linux()