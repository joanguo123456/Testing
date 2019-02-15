#coding utf-8

class GlobalVar:

    CaseID = 0
    name =1
    url = 2
    run = 3
    request_way = 4
    header = 5
    case_depend = 6
    data_depend = 7
    field_depend =8
    request_data = 9
    expect = 10
    result = 11

#获取caseID
def get_caseID():
    return GlobalVar.CaseID
#获取url
def get_url():
    return GlobalVar.url
#获取是否运行
def get_run():
    return GlobalVar.run
#获取请求方
def get_request_way():
    return GlobalVar.request_way
#获取header
def get_header():
    return GlobalVar.header
#
def get_case_depend():
    return GlobalVar.case_depend
#
def get_data_depend():
    return GlobalVar.data_depend
#
def get_field_depend():
    return GlobalVar.field_depend
#
def get_request_data():
    return GlobalVar.request_data
#
def get_expect():
    return  GlobalVar.expect
#
def get_result():
    return GlobalVar.result

#获取header的值
def get_header_value():
    header = {
        "header":"123456",
        "cookie":"guoguo"
    }
    return header