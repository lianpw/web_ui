from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import logging

from webdriver_helper import debugger

logger = logging.getLogger(__name__)


class KeyWord:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)  # 显示等待, 最多10s

    def find_element(self, *args):
        """
        封装元素定位方法, 自动使用显示等待
        :param args:
        :return:
        """
        logger.info(f'正在定位元素: {args}')
        el = self.wait.until(lambda _: self.driver.find_element(*args))
        logger.info('元素定位成功')
        return el

    def key_get_url(self, url):
        self.driver.get(url)

    def key_clikc(self, loc):
        """点击方法"""
        el = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        el.click()

    def key_input(self, loc, value=None):
        """输入方法"""
        el = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        # debugger(self.driver)
        el.clear()
        if value is not None:
            el.send_keys(value)

    def key_get_text(self, loc):
        el = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        text = el.text
        return text

    def key_assert_text(self, loc, text):
        el = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        el_text = el.text.strip()  # 去除两边的空格
        logger.info(f'元素的文本是{el_text}')
        text = text.strip()  # 去除两边空格
        logger.info(f'预期的文本是{text}')
        assert text == el_text

    def key_execute_sql(self, loc, code):
        el = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        self.driver.execute_script(code, el)