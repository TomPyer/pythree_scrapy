# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request, FormRequest
from pythree_scrapy.items import iFengNewItem


class IfengnewSpider(scrapy.Spider):
    name = 'ifengNew'
    allowed_domains = ['gz.house.ifeng.com']
    start_urls = ['http://gz.house.ifeng.com/news']

    def parse(self, response):
        # 第一步,获取左侧分类标题链接
        sel = Selector(response)
        title_type_div = sel.xpath('//div[@class="wleftfixbar"]')
        for li in title_type_div.xpath('.//ul[@class="wfixbar-list clearfix"]/li'):
            type_name = li.xpath('.//a/text()').extract_first(default='')
            type_url = li.xpath('.//a/@href').extract_first(default='')
            if type_name != '' and type_url != '':
                yield Request(type_url, self.two_parse, meta={'type_name': type_name})

    def two_parse(self, response):
        # 第二步,进入分类标题下,获取分类新闻列表
        sel = Selector(response)
        meta = response.meta
        new_div = sel.xpath('//div[@class="ni_list"]')
        for new_a in new_div.xpath('.//a'):
            new_url = new_a.xpath('.//@href').extract_first(default='')
            meta['time'] = new_a.xpath('.//dl/dd[@class="grey clearfix"]/span[@class="f1"]/text()').extract_first(default='')
            yield Request(new_url, self.three_parse, meta=meta)

    def three_parse(self, response):
        # 第三步,详细的新闻页面
        sel = Selector(response)
        meta = response.meta
        item = iFengNewItem()
        title_div = sel.xpath('//div[@class="title"]')
        item['title'] = title_div.xpath('.//h2/text()').extract_first(default='')
        item['time'] = meta['time']
        item['url'] = response.url
        item['news_type'] = meta['type_name']
        item['news_from'] = title_div.xpath('.//div[@class="pr"]/span/text()').extract_first(default='')
        item['content'] = '\n'.join(title_div.xpath('//div[@class="article"]/p/text()').extract())
        yield item


class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return
        # 日志功能使用
        self.logger.info('Parse function called on %s', response.url)