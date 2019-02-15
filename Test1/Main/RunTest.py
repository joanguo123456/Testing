#coding:utf-8
from Base.RunMethod import RunMethod
from Data.ReadData import ReadData
from Util.CommonDemo import CommonUtil
from Util.SendEmail import SendEmail
class RunTest:
    def __init__(self,filename,jsonname):
        self.run_method = RunMethod
        self.data = ReadData(filename,jsonname)

    #程序执行
    def go_on_run(self):
        pass_count = []
        fail_count = []
        row_count = self.data.get_case_line()
        for i in range(1,row_count):
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_case_run(i)
            header = self.data.is_header(i)
            data = self.data.get_data_by_key(i)
            expect = self.data.get_expect(i)
            if is_run ==True:
                res = str(self.run_method(url,method,data,header).res)
                if CommonUtil.is_contain(self,expect,res):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,'fail')
                    fail_count.append(i)
        SendEmail.send_mail(self,len(pass_count),len(fail_count))

        print('测试的case总数为：',row_count-1)
        print('测试通过的case个数为：',len(pass_count))
        print('测试失败的case个数为：',len(fail_count))




if __name__ == '__main__':
    run = RunTest('interfaceCase.xls','user.json')
    print(run.go_on_run())
