#coding:utf-8
import unittest
import os
import HTMLTestReportCN
from Base.testCase import TestMethod

if __name__ == '__main__':
    #创建容器，管理case
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path,'report/report.html')

    fp = open(file_path,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title="First Report",
        tester='joan'
    )
    runner.run(suite)
    fp.close()