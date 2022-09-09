import openpyxl


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

    suite_dict = {}  # 以套件名称为key, 以用例为value
    # 按行遍历
    for ws in wb.worksheets:
        case_dict = {}  # 以名称为key, 以步骤为value的字典
        case_name = ''
        for line in ws.iter_rows(values_only=True):
            _id = line[0]

            if isinstance(_id, int):
                if _id == -1:  # 用例名称
                    case_name = line[3]
                    case_dict[case_name] = []  # 以用例名称为key, 创建新的空用例
                elif _id > 0:  # 步骤
                    case_dict[case_name].append(filter_empty(line))  # 为用例填充步骤
        suite_dict[ws.title] = case_dict  # 本测试套件的所有用例
    return suite_dict # 格式化打印对象数据
