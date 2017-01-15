#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName:  html_downloader.py
@Author：liangzhicheng
@Createdate:  2017-01-14
@description： 网页输出器
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.separator = '\t'
        self.code = 'utf-8'

    def collect_data(self, data):
        '''
        收集相关数据
        :param data:[url:网页地址,title:标题,summary:内容]
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)

    def create_content(self, data):
        '''
        构造输出内容
        :param data:[url,title,summary]
        :return: 输出内容
        '''
        content = data['url'].encode(self.code) + self.separator + data['title'].encode(self.code) + self.separator + \
                  data[
                      'summary'].encode(self.code).replace('\n', '') + '\n'
        return content

    def output_xlsx(self, fileName):
        '''
        将收集的数据输出成xlsx文件
        :return:
        '''
        fout = open(fileName + '.xlsx', 'w+')
        fout.write('url' + self.separator + 'title' + self.separator + 'summary' + '\n')
        for data in self.datas:
            content = self.create_content(data)
            fout.write(content)
        fout.close()
