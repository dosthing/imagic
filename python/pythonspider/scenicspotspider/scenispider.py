#!/usr/bin/env python
# encoding: utf-8
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import ssl
import re

# url管理器
class UrlManager(object):

    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    # 添加 url
    def add_new_url(self, url):
        if url is None:
            return

        if url not in self.new_url or url not in self.old_url:
            self.new_url.add(url)

    # 添加新的 url
    def add_new_urls(self, urls):
        if urls is None:
            return

        for url in urls:
            self.new_url.add(url)

    # 判断是否存在新的 url
    def has_new_url(self):
        return len(self.new_url) != 0

    # 获取新的 url
    def get_new_url(self):
        new_url = self.new_url.pop()
        self.old_url.add(new_url)
        return new_url

# url下载器		
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        # 打开新的 URL
        response = request.urlopen(url)

        # 判断返回值
        if response.getcode() != 200:
            return None

        # 返回内容
        return response.read()

# url 解析器		
class UrlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.find_all('a', href=re.compile(r'/item/*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title">      <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        #res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        #summary_node = soup.find('div', class_='lemma-summary')
        #res_data['summary'] = summary_node.get_text()
		
		#<div class="basic-info cmn-clearfix" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='basic-info cmn-clearfix')
        #print(summary_node.get_text())
        #res_data['summary'] = summary_node.get_text()

        #<dt class="basicInfo-item name">景点级别</dt>
        scenic_nodes = soup.find_all('dt', class_=re.compile(r'basicInfo-item *'))
        #print (len(scenic_nodes))
        for scenic_node in scenic_nodes:
            if '景点级别' in scenic_node.get_text():
                print (scenic_node.get_text())
                #res_data['url'] = page_url
                res_data['title'] = title_node.get_text()
                res_data['summary'] = summary_node.get_text()
                return res_data
        return None

    def parse(self, page_url, html_cont):
        # 判断 URL 和 cont 是否为 None
        if page_url is None or html_cont is None:
            return None

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

# 结果输出器
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open('out_put.html', 'w', encoding='utf-8')

        fout.write('<head>')
        fout.write('<body>')
        fout.write('<table style="border-color:#33A0E8;" border="1px"; align="center">')

        # Python 默认编码格式是： Ascii
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td width="180px" height="auto" align="center">%s</td>' % data['title'])
            fout.write('<td width="80px" height="auto" align="center"> <a href=%s>景点详情</a></td>' % data['url'])            
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</head>')
        fout.close()

class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()#url_manager.UrlManager()
        self.downloader = HtmlDownloader()#html_downloader.HtmlDownloader()
        self.outputer = HtmlOutputer()#html_outputer.HtmlOutputer()
        self.parser = UrlParser()#html_parser.UrlParser()

    def craw(self, root_url):
        count = 1

        # 添加 url
        self.urls.add_new_url(root_url)

        # 当 urls 存在 url 的时候进入循环，否则不进入
        while self.urls.has_new_url():
            try:
                # 获取新的 url
                new_url = self.urls.get_new_url()

                print('craw %d : %s' % (count, new_url))

                # 下载新的 url 的内容
                html_cont = self.downloader.download(new_url)
                # 解析 url 和 数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将新页面的 url 添加到 url 中
                self.urls.add_new_urls(new_urls)
                # 输入器进行数据的收集
                self.outputer.collect_data(new_data)

                # 数据条数可以自行设置，条目越多花费时间越长
                if count == 2000:
                    break
                count += 1

            except:
                print('craw failed.')

        self.outputer.output_html()


if __name__ == '__main__':
    # 程序入口的爬虫
    #root_url = 'https://baike.baidu.com/item/Python/407313'
    root_url = 'https://baike.baidu.com/item/%E7%99%BD%E4%BA%91%E5%B1%B1/1365'
    spider = SpiderMain()
    spider.craw(root_url)