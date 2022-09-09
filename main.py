import os
import pytest


if __name__ == '__main__':
    pytest.main(['-vs'])
    os.system("allure generate ./temps/allure -o reports --clean")  # 生成报告
    # os.system('allure open reports -p 0')  # 打开报告