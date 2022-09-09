from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import logging

from webdriver_helper import debugger

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)  # 显示等待, 最多10s

        self.check_element()

    def check_element(self):
        """
        把属性中的字符串, 变成真正的元素
        检查是否有元素丢失
        :return:
        """
        for attr in dir(self):
            # print(attr)
            if attr.startswith("ele_"):  # 校验是否是我们定义的元素属性
                loc = getattr(self, attr)  # 获取属性值
                el = self.find_element(By.XPATH, loc)  # 定位元素
                setattr(self, attr, el)  # 设置属性, 把属性值变成元素

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

    def base_clikc(self, el: WebElement):
        """点击方法"""
        self.wait.until(lambda _: el.is_enabled())
        el.click()

    def base_input(self, el: WebElement, value=None):
        """输入方法"""
        self.wait.until(lambda _: el.is_enabled())
        el.clear()
        if value is not None:
            el.send_keys(value)

    def base_get_msg(self):
        msg = self.find_element(By.XPATH, '/html/body/div[10]/div/p').text
        return msg

    def base_get_text(self, el: WebElement):
        self.wait.until(lambda _: el.is_enabled())
        text = el.text
        return text

# 首页
class HomePage(BasePage):
    ele_login_link = '/html/body/div[2]/div/ul[1]/div/div/a[1]'

    def to_login(self):
        """跳转到登录页面"""
        self.base_clikc(self.ele_login_link)
        # 因为登录case涉及首页和登录两个页面. 所以需要共用一个driver, 在首页直接将driver传给登录页
        return LoginPage(self.driver)


# 登录页面
class LoginPage(BasePage):
    ele_login_username = '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input'
    ele_login_password = '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input'
    ele_login_btn = '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button'

    def login(self, username, password):
        self.base_input(self.ele_login_username, username)
        self.base_input(self.ele_login_password, password)
        self.base_clikc(self.ele_login_btn)


# 商品详情页面
class GoodsDetailPage(BasePage):
    ele_collect_btn = '/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[1]'
    ele_collect_num = '/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[2]'

    def collect(self):
        self.base_clikc(self.ele_collect_btn)

    def get_collect_num(self):
        text = self.base_get_text(self.ele_collect_num)
        num = int(text.replace('(', '').replace(')', ''))
        return num


# 商品收藏页
class UseGoodsCollectPage(BasePage):
    ele_select_all_btn = '/html/body/div[4]/div[3]/div/div[2]/form/div[3]/table/thead/tr[1]/th[1]/button'
    ele_del_btn = '/html/body/div[4]/div[3]/div/div[2]/form/div[2]/button[1]'
    # 因为确定框刚开始没有出现, 所以不能自动定位, 否则会报错, 将前缀改成loc
    loc_confirm_btn = '//span[text()="确定"]'  # 改定位元素会变化, 可以通过debugger进行排查

    def delete_all(self):
        if self.ele_select_all_btn.is_enabled():
            self.base_clikc(self.ele_select_all_btn)
            self.base_clikc(self.ele_del_btn)
            # debugger(self.driver)
            # loc前缀的元素, 不会自动定位
            self.base_clikc(self.find_element(By.XPATH, self.loc_confirm_btn))
            return True
        else:
            return False
