"""
@Filename:  core/setting
@Author:   lianpengwei
@Time:    2022/9/15 15:05
@Describe:  处理配置文件
"""
from pathlib import Path

from iniconfig import IniConfig
from pydantic import BaseSettings, DirectoryPath


class UiSettings(BaseSettings):
    # allure报告保存位置
    allure_report: DirectoryPath = './reports'
    # 生成报告之后是否自动打开报告
    allure_show: bool = True
    # 显示等待超时时间
    wait_max: float = 10
    # 显示等待轮询频率
    wait_poll: float = 0.1
    # 浏览器类型
    driver_type: str = 'chrome'


def load_ini():
    path = Path('pytest.ini')
    if not path.exists():
        return {}
    ini = IniConfig('pytest.ini')
    if 'uitest' not in ini:
        return {}

    data = dict(ini['uitest'].items())
    return data


ui_setting = UiSettings(**load_ini())