# -*- coding: UTF-8 -*-

import xlrd
from config import root_path
import xlwt
data_path = root_path + "\\testData\\test_data.xlsx"

def getXlsData(path,sheet_name,module):

    xlsf = xlrd.open_workbook(path)
    sheet = xlsf.sheet_by_name(sheet_name)
    rows = sheet.nrows
    clos = sheet.ncols
    listdate = []
    for row in  range(1,rows):
        dict_data = {}
        if sheet.cell(row,2).value == module:
         # print sheet.cell(row,2).value
         dict_data['casename'] = sheet.cell(row,1).value
         dict_data.update(eval(sheet.cell(row,3).value))
         dict_data.update(eval(sheet.cell(row,4).value))
         listdate.append(dict_data)
    return listdate

if __name__=='__main__':
    print getXlsData(data_path,'login','login')