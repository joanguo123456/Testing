#coding；utf-8
from Util.ExcelDemo import OperationExcel
from Util.JsonDemo import OperationJson
import Util.ConfigData
import os

class ReadData:
    def __init__(self,excelname=None,jsonname=None,emailname=None):
        self.filename = os.path.join('E:/20181213基础/接口/unittest/Base/config/',excelname)
        self.jsonname = os.path.join('E:/20181213基础/接口/unittest/Base/config/',jsonname)
        self.oper_excel = OperationExcel(self.filename)
        self.oper_json = OperationJson(self.jsonname)

    #获取case个数
    def get_case_line(self):
        return self.oper_excel.get_lines()
    #获取是否执行
    def get_case_run(self,row):
        flag = None
        col = Util.ConfigData.get_run()
        run_model = self.oper_excel.get_cell(row,col)
        if run_model == 'yes':
            flag =  True
        else:
            flag =  False
        return flag
    #是否携带header
    def is_header(self,row):
        col  = Util.ConfigData.get_header()
        header_module = self.oper_excel.get_cell(row,col)
        if header_module == "yes":
            return Util.ConfigData.get_header_value()
        else:
            return None


    #获取请求方式
    def get_request_method(self,row):
        col = Util.ConfigData.get_request_way()
        request_methd = self.oper_excel.get_cell(row,col)
        return request_methd
    #获取url
    def get_url(self,row):
        col = Util.ConfigData.get_url()
        url = self.oper_excel.get_cell(row,col)
        return url

    # 获取请求数据
    def get_request_data(self,row):
        col = Util.ConfigData.get_request_data()
        data = self.oper_excel.get_cell(row,col)
        if data == " ":
            return None
        else:
            return data

    #根据关键字获取jason数据
    def get_data_by_key(self,row):
        key_data = self.oper_json.get_data(self.get_request_data(row))
        return key_data
    #获取预期结果
    def get_expect(self,row):
        col = Util.ConfigData.get_expect()
        expect = self.oper_excel.get_cell(row,col)
        if expect ==" ":
            return None
        else:
            return expect
    #写入result
    def write_result(self,row,value):
        col = Util.ConfigData.get_result()
        result = self.oper_excel.write_cell(row,col,value)
        return result


if __name__ == "__main__":
    data = ReadData('interfaceCase.xls','user.json','email.ini')
    print(data.emailname)
    print(data.get_case_line())
    print(data.get_case_run(2))
    print(type(data.get_url(2)))
    print(data.is_header(2))
    print(type(data.get_request_method(2)))
    print(type(data.get_request_data(2)))
    print(data.get_expect(2))
    print(type(data.get_data_by_key(2)))
    print(data.read_config('send','sender'))
