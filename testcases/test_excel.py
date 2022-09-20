import sys
import logging
from pathlib import Path

from core.case import create_case
from core.read_data import read_excel


logger = logging.getLogger(__name__)

# test_dir = Path(__file__)  # D:\workspace\mashang_project\web_ui_three\testcases\test_excel.py
test_dir = Path(__file__).parent  # D:\workspace\mashang_project\web_ui_three\testcases
_case_count = 0  # 用例数量
file_list = test_dir.glob("test_*.xlsx")  # 自动收集excel文件
# print(list(file_list))

for file in file_list:
    data = read_excel(file)
    for case, suite_name in create_case(data, file):
        _case_count += 1
        globals()[f'Test_{_case_count}_{suite_name}'] = case
logger.info('所有excel测试用例执行完成')