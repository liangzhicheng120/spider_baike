#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName:  spider_main.py
@Author：liangzhicheng
@Createdate:  2017-01-15
@description： 爬虫调度端
'''
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        '''
        初始化各个对象
        '''
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 页面下载器
        self.parser = html_parser.HtmlParser()  # 页面解析器
        self.outputer = html_outputer.HtmlOutputer()  # 页面输出器

    def craw(self, root_url, url_num, output_name):
        '''
        抓取网页
        :param root_url: 根url
        :param url_num: 抓取url的个数
        :return:
        '''
        count = 1  # url 计数器
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 获取一个待爬取的url
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 下载一个页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)  # 将新的url添加到url管理器
                self.outputer.collect_data(new_data)  # 提取页面数据
                if count == url_num:
                    break
                count = count + 1
            except:
                print 'craw failed'  # 处理无法爬取的url

        self.outputer.output_xlsx(output_name)  # 将收集的数据输出成xlsx


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, 10, 'output')
