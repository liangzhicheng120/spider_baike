#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName: test_url_manager.py
@Author：liangzhicheng
@Createdate:  2017-01-15
@description： 测试URL管理器
'''
from main.url_manager import UrlManager
import unittest


class TestUrlManager(unittest.TestCase):
    def setUp(self):
        '''
        初始化url管理器
        :return:
        '''
        self.url_manager = UrlManager()

    def tearDown(self):
        '''
        关闭url管理器
        :return:
        '''
        self.url_manager = None

    def test_add_new_url(self):
        '''
        测试添加新的url
        :return:
        '''
        self.assertEqual(self.url_manager.add_new_url(None), None)

    def test_has_new_url(self):
        '''
        测试判断是否有url
        :return:
        '''
        self.assertEqual(self.url_manager.has_new_url(), False)

    def test_get_new_url(self):
        '''
        测试获取一个url
        :return:
        '''
        self.url_manager.add_new_url('www.baidu.com')
        self.assertEqual(self.url_manager.get_new_url(), 'www.baidu.com')


if __name__ == '__main__':
    unittest.main()
  
