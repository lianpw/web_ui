from pprint import pprint

import openpyxl

from core.read_data import read_excel

if __name__ == '__main__':
    data = read_excel('testcases/test_excel.xlsx')
    pprint(data)