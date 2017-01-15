#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName: url_manager.py
@Author：liangzhicheng
@Createdate:  2017-01-15
@description： URL管理器
'''


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        '''
        添加一个新的url
        :param url: url
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:  # 全新的url
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        批量添加url
        :param urls: url列表
        :return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        '''
        判断是否有新的url
        :return:true or false
        '''
        return len(self.new_urls) != 0

    def get_new_url(self):
        '''
        获取一个新的url
        :return:a new url
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
