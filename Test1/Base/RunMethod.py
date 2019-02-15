#coding:utf-8
import requests
import json

class RunMethod:
    def __init__(self,url,method,data=None,header=None):
        self.res = self.run_main(url,method,data,header)
    def post_main(self,url,data,header=None):
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def get_main(self,url,data=None,header=None):
        if header != None:
            res = requests.get(url=url,data=data,headers=header).json()
        else:
            res = requests.get(url=url,data=data).json()
            print(type(res))
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None,header=None):
        if method =="GET":
            res = self.get_main(url,data,header)
        else:
            res = self.post_main(url,data,header)
        return json.loads(res)

if __name__ == '__main__':

    url = 'https://coding.imooc.com/api/testcdn'
    data = {
        'apiname':'testcdn',
        'secrect':'ae886c433298c2ac1f8c6c3370855505',
        'timestamp':'1549002087150',
        'token':'46190ea8a02081b226f7c1880b90972e',
        'uid':'7400228'
    }

    res = RunMethod(url,'post',data).res


    print(res)
    print(res["errorCode"])