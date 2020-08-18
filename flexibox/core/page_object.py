# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Browserobject this to create generic methods to
#          manipulate page objects in a browser
# Download the latest gecko driver object
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from flexibox.core.logger import Logger


class Pageobject(object):
    def __init__(self):
        self.log = Logger()

    # Get element by id
    def get_element_by_id(self, driver, id):
        try:
            driver.find_element_by_id(id)
            self.log.log_info("Element with attribute id is traced on the web page")
        except NoSuchElementException:
            self.log.log_error("Attribute ID is not present on the web page")

    # Get element by name
    def get_element_by_name(self, driver, name):
        try:
            driver.find_element_by_name(name)
            self.log.log_info("Element with attribute name is traced on the web page")
        except NoSuchElementException:
            self.log.log_error("Attribute NAME is not present on the web page")

    # Get element by xpath
    def get_element_by_xpath(self, driver, xpath):
        try:
            driver.find_element_by_xpath(driver, xpath)
            self.log.log_error("Element with the XPATH is traced on the web page")
        except NoSuchElementException:
            self.log.log_error("Element with the XPATH is not present on the web page")

    # Get element by link text
    def get_element_by_linktext(self, driver, link_text):
        try:
            driver.find_element_by_link_text(link_text)
            self.log.log_info("LINK TEXT is found on the web page")
        except NoSuchElementException:
            self.log.log_error("LINK TEXT is not present on the web page")

    # Get element by partial link text
    def get_element_by_partial_linktext(self, driver, partial_link_text):
        try:
            driver.find_element_by_link_text(partial_link_text)
            self.log.log_info("PARTIAL LINK TEXT is found on the web page")
        except NoSuchElementException:
            self.log.log_error("PARTIAL LINK TEXT is not present on the web page")

    # Get element by tag name
    def get_element_by_tagname(self, driver, tag_name):
        try:
            driver.find_element_by_tag_name(tag_name)
            self.log.log_info("TAG NAME is present on the web page")
        except NoSuchElementException:
            self.log.log_error("TAG NAME is not present on the web page")

    # Get element by class name
    def get_element_by_class_name(self, driver, class_name):
        try:
            driver.find_element_by_class_name(class_name)
            self.log.log_info("CLASS NAME is not found on the web page")
        except NoSuchElementException:
            self.log.log_error("CLASS NAME is not present on the web page")

    # Get element by css selector
    def get_element_by_css_selector(self, driver, selector):
        try:
            driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            self.log.log_error("CSS SELECTOR is not present in the web page")

    # Return elements by name as a list
    def get_elements_by_name(self, driver, name):
        try:
            driver.find_elements_by_name(name)
            self.log.log_info("Elements with attribute NAME is traced on the web page")
        except NoSuchelementsException:
            self.log.log_error("Attribute NAME is not present on the web page")

    # Return elements by xpath as a list
    def get_elements_by_xpath(self, driver, xpath):
        try:
            driver.find_elements_by_xpath(driver, xpath)
            self.log.log_error("Elements with the XPATH is traced on the web page")
        except NoSuchelementsException:
            self.log.log_error("Elements with the XPATH is not present on the web page")

    # Return elements by link text as a list
    def get_elements_by_linktext(self, driver, link_text):
        try:
            driver.find_elements_by_link_text(link_text)
            self.log.log_info("LINK TEXT is found on the web page")
        except NoSuchelementsException:
            self.log.log_error("LINK TEXT is not present on the web page")

    # Return elements by partial link text as a list
    def get_elements_by_partial_linktext(self, driver, partial_link_text):
        try:
            driver.find_elements_by_link_text(partial_link_text)
            self.log.log_info("PARTIAL LINK TEXT is found on the web page")
        except NoSuchelementsException:
            self.log.log_error("PARTIAL LINK TEXT is not present on the web page")

    # Return elements by tag name as a list
    def get_elements_by_tagname(self, driver, tag_name):
        try:
            driver.find_elements_by_tag_name(tag_name)
            self.log.log_info("TAG NAME is present on the web page")
        except NoSuchelementsException:
            self.log.log_error("TAG NAME is not present on the web page")

    # Return elements by class name as a list
    def get_elements_by_class_name(self, driver, class_name):
        try:
            driver.find_elements_by_class_name(class_name)
            self.log.log_info("CLASS NAME is not found on the web page")
        except NoSuchelementsException:
            self.log.log_error("CLASS NAME is not present on the web page")

    # Return elements by css selector as a list
    def get_elements_by_css_selector(self, driver, selector):
        try:
            driver.find_elements_by_css_selector(selector)
        except NoSuchelementsException:
            self.log.log_error("CSS SELECTOR is not present in the web page")
