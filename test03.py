"""
@Filename:  /test03
@Author:   lianpengwei
@Time:    2022/9/14 12:03
@Describe:  ...
"""
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    def __init__(self, request=None):
        self.request = request

    def base_fixture(self, fixtrue_name):
        driver = self.request.getfixturevalue(fixtrue_name)
        self.get_driver(driver)

    def get_driver(self, driver: WebDriver):
        self.driver = driver
        self.driver.maximize_window()
