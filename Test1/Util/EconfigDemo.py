import configparser
import os

class OperateEconfig:
    def __init__(self,filename=None):
        if filename == None:
            self.filename = os.path.join('E:/20181213基础/接口/unittest/Base/config/','email.ini')
        else:
            self.filename = os.path.join('E:/20181213基础/接口/unittest/Base/config/',filename)
    #读取邮件信息的配置文件,根据字段和关键字返回数据
    def read_config(self,section,key):
        config = configparser.ConfigParser()
        config.read(filenames=self.filename,encoding='utf-8')
        config_data = config.get(section,key)
        return config_data
    #读取邮件信息的配置文件，读取某section下的全部数据
    def read_section(self,section):
        config = configparser.ConfigParser()
        config.read(filenames=self.filename,encoding='utf-8')
        config_data = config.options(section)
        return config_data

    #将全部收件人遍历生成序列
    def get_addkey(self, addresser):
        '''遍历获得配置文件收件人email'''
        sum = 0
        address_list = []
        for i in addresser:
            if sum < len(addresser):
                emails = self.read_config('addressed', i)
                address_list.append(emails)
                sum += 1
        return address_list