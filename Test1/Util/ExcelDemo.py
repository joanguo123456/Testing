#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy

#data_excel = xlrd.open_workbook('config/interfaceCase.xlsx')
#tables = data_excel.sheet_by_index(0) #获取第一个sheet
#print(tables.nrows) #打印sheet的列数
#print(tables.cell(2,2))#

class OperationExcel:
    def __init__(self,filename=None,sheet_id=None):
        self.filename = filename
        if sheet_id == None:
            self.sheet_id = 0
        else:
            self.sheet_id = sheet_id
        self.table = self.get_table()
    #获取表的内容
    def get_table(self):
        data_excel = xlrd.open_workbook(self.filename)
        table = data_excel.sheet_by_index(self.sheet_id)
        return table
    #获取表的行数
    def get_lines(self):
        table = self.get_table()
        return table.nrows
    #获取某个单元格的内容
    def get_cell(self,row,col):
        return self.get_table().cell(row,col).value
    #单元格写入内容
    def write_cell(self,row,col,value):
        #写入excel
        book1 = xlrd.open_workbook(self.filename)
        book2 = copy(book1)
        sheet = book2.get_sheet(0)
        sheet.write(row,col,value)
        book2.save(self.filename)





if __name__ =="__main__":
    oper =  OperationExcel('E:/20181213基础/接口/unittest/Base/config/interfaceCase.xlsx',0)
    tables = oper.get_table()
    print(oper.get_lines())
    print(oper.get_cell(2,2))
    print(oper.write_cell(2,11,'tongugo'))
    print(oper.get_cell(2,11))

