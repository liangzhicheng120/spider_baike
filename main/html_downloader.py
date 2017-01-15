#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName:  html_downloader.py
@Author：liangzhicheng
@Createdate:  2017-01-14
@description： 网页下载器
'''
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        '''
        下载网页
        :param url: url网址
        :return:
        '''
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
