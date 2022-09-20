import openpyxl
import logging


logger = logging.getLogger(__name__)


def filter_empty(old_l):
    """过滤序列中的空值"""
    new_l = []
    for i in old_l:
        if i:
            new_l.append(i)
    return new_l

def read_excel(path):
    wb = openpyxl.load_workbook(path)  # 加载excel
    # ws = wb.active  # 读取当前工作表
    logger.info(f'文件{path=}, 包含{len(wb.worksheets)}个sheet')
    suite_dict = {}  # 以套件名称为key, 以用例为value
    for ws in wb.worksheets:
        case_dict = {}  # 以名称为key, 以步骤为value的字典
        case_name = ''
        # 按行遍历
        for line in ws.iter_rows(values_only=True):
            logger.debug(f'正在处理行: {line}')
            _id = line[0]

            if isinstance(_id, int):
                if _id == -1:  # 用例名称
                    case_name = line[3]
                    case_dict[case_name] = []  # 以用例名称为key, 创建新的空用例
                elif _id > 0:  # 步骤
                    case_dict[case_name].append(filter_empty(line))  # 为用例填充步骤
        logger.info(f'sheet:{ws.title}, 包含{len(case_dict)}个用例')
        suite_dict[ws.title] = case_dict  # 本测试套件的所有用例
    logger.debug(f'加载完成测试用例{suite_dict=}')
    return suite_dict # 格式化打印对象数据
