import json
from json.decoder import JSONDecodeError
from pathlib import Path

import pytest
from webdriver_helper import get_webdriver

from core import pom


@pytest.fixture(scope='class')
def driver():
    d = get_webdriver()  # 启动浏览器
    yield d
    d.quit()  # 关闭浏览器


@pytest.fixture(scope='session')
def login_driver():
    """
    返回已登录的浏览器
    :return:
    """
    driver = get_webdriver()
    driver.get('http://101.34.221.219:8010/')
    cookies = []
    path = Path('temps/cookies/cookies.json')
    if path.exists():
        try:
            with open('temps/cookies/cookies.json', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
        except JSONDecodeError:
            pass
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()  # 刷新, 检查登录状态

    if "退出" not in driver.page_source:
        home_page = pom.HomePage(driver)
        login_page = home_page.to_login()  # 跳转到登录页面
        login_page.login('test101', '123456')
        msg = login_page.base_get_msg()
        assert msg == '登录成功'

        # 保存cookie到临时文件
        cookies = driver.get_cookies()
        with open('temps/cookies/cookies.json', 'w') as f:
            json.dump(cookies, f)
    yield driver
    driver.quit()


@pytest.fixture()
def clear_collect_goods(login_driver):
    """
    清除收藏的商品
    :return:
    """
    login_driver.get('http://101.34.221.219:8010/?s=usergoodsfavor/index.html')
    user_goods_collect_page = pom.UseGoodsCollectPage(login_driver)
    is_click = user_goods_collect_page.delete_all()
    if is_click:
        msg = user_goods_collect_page.base_get_msg()
        assert msg == '删除成功'
    yield login_driver
