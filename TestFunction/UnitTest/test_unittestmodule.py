from browserium.chromedriver import Chromedriver
from nose.tools import assert_equals
from nose.tools import assert_true
import os
import wget
import requests

class UnittestModule(Chromedriver):

    def AssertEquals(self,actual,expected):
        assert_equals(actual, expected)

    def AssertTrue(self, result):
        assert_true(result)

    def test_api_chromedriver_mac(self):
        api_url_mac = self.url_builder('_mac')
        response = requests.get(api_url_mac)
        self.AssertEquals(response,"200")
        wget.download(api_url_mac)
        result = os.path.exists("chromedriver_mac64.zip")
        self.AssertTrue(result)

    def test_api_chromedriver_linux(self):
        api_url_linux = self.url_builder("_linux")
        response = requests.get(api_url_linux)
        self.AssertEquals(response,"200")
        wget.download(api_url_linux)
        result = os.path.exists("chromedriver_linux64.zip")
        self.AssertTrue(result)