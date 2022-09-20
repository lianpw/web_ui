"""
@Filename:  /test04
@Author:   lianpengwei
@Time:    2022/9/14 18:12
@Describe:  ...
"""
import pytest


class TestManager(object):

    # 针对特定的用例调用固件
    @pytest.mark.parametrize('name', ['lian', 'pan'], ids=['xiao', 'da'])
    def test_(self,name):  # 固件有别名时, 需要使用别名
        print('mashang')
        print(name)  # 使用固件的参数

    # def test_jiaoyu(self):
    #     print('jiaoyu')
    #
    # def test_ceshi(self):
    #     print('ceshi')