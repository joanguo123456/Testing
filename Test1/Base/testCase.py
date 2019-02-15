# coding:utf-8
import unittest
from Base.requestDemo import RunMain
from unittest import mock


class TestMethod(unittest.TestCase):
    #def setUp(self):
      #  run = RunMain
    def test_01(self):
        url = 'https://coding.imooc.com/api/testcdn'
        data = {
            'apiname': 'testcdn',
            'secrect': 'ae886c433298c2ac1f8c6c3370855505',
            'timestamp': '1549002087150',
            'token': '46190ea8a02081b226f7c1880b90972e',
            'uid': '7400228'
        }
        mock_data= mock.Mock(return_value = data)
        print(mock_data)
        RunMain.run_main = mock_data
        res = RunMain.run_main(url,'post',data)
        #res = RunMain(url, 'post', data).res
       # self.assertEqual(res['errorCode'],1000,'测试失败')
        print(res)
        print('第一个测试')

    @unittest.skip('test_02')
    def test_02(self):
        url = 'https://coding.imooc.com/api/testcdn'
        data = {
            'apiname': 'testcdn',
            'secrect': 'ae886c433298c2ac1f8c6c3370855505',
            'timestamp': '1549002087150',
            'token': '46190ea8a02081b226f7c1880b90972e',
            'uid': '7400228'
        }
        print('第二个测试')
        res = RunMain(url, 'post', data).res
        self.assertEqual(res['errorCode'],1000,'测试失败')

