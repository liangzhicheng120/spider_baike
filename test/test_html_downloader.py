#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName: test_html_downloader.py
@Author：liangzhicheng
@Createdate:  2017-01-15
@description： 测试网页下载器
'''
import unittest
from main.html_downloader import HtmlDownloader


class TestHtmlDownLoader(unittest.TestCase):
    def setUp(self):
        self.html_downloader = HtmlDownloader()

    def tearDown(self):
        self.html_downloader = None

    def test_download(self):
        '''
        测试网页下载器
        :return:
        '''
        self.assertEqual(self.html_downloader.download(None), None)


if __name__ == '__main__':
    unittest.main()
