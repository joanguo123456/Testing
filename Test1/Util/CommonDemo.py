#coding:utf -8

class CommonUtil:
    #判断字符串1在字符串2中
    def is_contain(self,str1,str2):
        flag = None
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag
