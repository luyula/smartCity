# -*- coding: UTF-8 -*-
import unittest

import testCase.test_login, testCase.test_material
from commonBase.HTMLTestRunner_cn import HTMLTestRunner
import time


def createReport():
    suite = unittest.TestSuite()
    suite.addTest(testCase.test_login.TestLogin('test_pswIsNull'))
    # suite.addTest(testCase.test_login.TestLogin("test_userIsNull"))
    # suite.addTest(testCase.test_login.TestLogin("test_pswIsError"))
    # suite.addTest(testCase.test_login.TestLogin("test_loginSuccess"))
    # suite.addTest(testCase.test_material.TestMaterial("test_createFile"))


    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    f_path = "C:\\Users\\ancey\\PycharmProjects\\myproject\\testReport\\%s.html" %now
    re_open = open(f_path,'wb')
    runner = HTMLTestRunner(stream=re_open,title=u'智慧城市_Report',description=u'引用测试报告模板')
    runner.run(suite)


