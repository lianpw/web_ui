from pathlib import Path

import allure
import pytest
import logging
from webdriver_helper import get_webdriver

from core.kdt import KeyWord


logger = logging.getLogger(__name__)


def create_case(test_suite: dict, file):
    file_path = Path(file)
    file_name = file_path.name

    for suite_name, case_dict in test_suite.items():
        @allure.suite(file_name)
        class Test:
            # 把pytest夹具保存到测试类当中
            @pytest.fixture(autouse=True)
            def init_fixture(self, request):
                self.request = request

            @pytest.mark.parametrize('case', case_dict.items(), ids=case_dict.keys())
            def test_(self, case):
                name = case[0]  # 用例名称
                step_list = case[1]  # 用例步骤
                # print(f'{name=}')
                # print(f'{step_list=}')

                kw = KeyWord(request=self.request)  # 不传递driver, 传递pytest
                for step in step_list:
                    key = step[2]  # 关键字
                    args = step[3:]  # 关键字参数
                    # print(f'{key=}')
                    # print(f'{args=}')
                    f = kw.get_kw_method(key)
                    try:
                        with allure.step(step[1]):
                            f(*args)  # 调用关键字方法
                    except Exception as e:
                        logger.error('关键字调用出错', exc_info=True)
                        raise e
                    finally:
                        allure.attach(kw.driver.get_screenshot_as_png(), step[1], allure.attachment_type.PNG)
        yield Test, suite_name  # 返回用例