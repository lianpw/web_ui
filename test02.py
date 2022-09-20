from pprint import pprint

import openpyxl

from core.read_data import read_excel

if __name__ == '__main__':
    data = read_excel('testcases/lian_test_excel.xlsx')
    # pprint(data)
    for suite_name, case_dict in data.items():
        # print(case_dict)
        # print()
        for i in case_dict.items():
            print(i)
            print()