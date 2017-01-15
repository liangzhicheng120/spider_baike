#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
'''
@FileName:  html_parser.py
@Author：liangzhicheng
@Createdate:  2017-01-14
@description： 网页解析器
'''
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        '''
        处理抓取网页上的数据
        :param page_url: 网页上的url链接
        :param html_cont: 已下载的网页
        :return: 待抓取的url列表,待处理数据字典
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        获取新的url列表
        :param page_url: 网页上的url
        :param soup: soup对象
        :return: 待抓取的url列表
        '''
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        获取待处理的数据
        :param page_url: 网页上的url
        :param soup: soup对象
        :return: 待处理的数据字典
        '''
        res_data = {}

        res_data['url'] = page_url
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data
