# -*- coding: utf-8 -*-
import scrapy
from scrapy import Item, Field
from scrapySpider.items import Xicidaili
from scrapy.contrib.spiders import CrawlSpider,Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class XicidailiSpider(scrapy.Spider):
    name = "xicidaili"
    allowed_domains = ["xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/nn/1']

    # rules = [ # 定义爬取URL的规则
    #     Rule(SgmlLinkExtractor(allow=("nn/[0-9]+")), follow=True, callback='parse')
    # ]

    def start_requests(self):
        res = []
        for i in range(1, 1149):
            url = 'http://www.xicidaili.com/nn/%d'%i
            req = scrapy.Request(url)
            # 存储所有对应地址的请求
            res.append(req)
        return res

    def parse(self, response):
        page = response.xpath('//div[@class="pagination"]//a[last()-1]//text()').extract()[0]
        #self.start_requests(page)
        table = response.xpath('//table[@id="ip_list"]')[0]
        trs = table.xpath('//tr')[1:]   #去掉标题行
        items = []
        for tr in trs:
            item = Xicidaili()
            item['ip'] = tr.xpath('td[2]/text()').extract()[0]
            item['port'] = tr.xpath('td[3]/text()').extract()[0]
            item['position'] = tr.xpath('string(td[4])').extract()[0].strip()
            #item['position'] = tr.xpath('td[4]/a[1]/text()').extract()[0]
            item['anonymous'] = tr.xpath('td[5]/text()').extract()[0]
            item['type'] = tr.xpath('td[6]/text()').extract()[0]
            item['speed'] = tr.xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            item['connect_time'] = tr.xpath('td[8]/div/@title').re('\d+\.\d*')[0]
            item['last_check_time'] = tr.xpath('td[10]/text()').extract()[0]
            items.append(item)
        return items

