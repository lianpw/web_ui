from pathlib import Path

from core import pom
import os


class TestWeb:

    def test_login(self, driver):  # driver是在夹具中生成的
        driver.get('http://101.34.221.219:8010/')
        home_page = pom.HomePage(driver)
        login_page = home_page.to_login()  # 跳转到登录页面
        login_page.login('test101', '123456')
        msg = login_page.base_get_msg()
        assert msg == '登录成功'

    def test_goods_collect(self, clear_collect_goods):
        clear_collect_goods.get('http://101.34.221.219:8010/?s=goods/index/id/5.html')
        goods_detail_page = pom.GoodsDetailPage(clear_collect_goods)
        collect_count = goods_detail_page.get_collect_num()  # 收藏之前获取收藏数量
        goods_detail_page.collect()
        msg = goods_detail_page.base_get_msg()
        assert msg == '收藏成功'
        new_collect_count = goods_detail_page.get_collect_num()  # 收藏之后的收藏数量
        assert new_collect_count - collect_count == 1  # 断言收藏之后的数量变化