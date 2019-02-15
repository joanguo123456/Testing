#coding:utf-8
import json
'''
fp = open('config/user.json')
json_data = json.load(fp)
print(json_data['login'])
'''
class OperationJson:
    def __init__(self,filename):
        self.filename = filename
        self.data = self.read_json()
    #读取json文件
    def read_json(self):
        with open(self.filename) as fp:
            json_data = json.load(fp)
        return json_data
    #根据关键字获取数据
    def get_data(self,key):
        return self.data[key]

if __name__ =="__main__":
    opjson = OperationJson('E:/20181213基础/接口/unittest/Base/config/user.json')
    print(opjson.data['user'])
    print(opjson.get_data('user'))