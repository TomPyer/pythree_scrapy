# -*- coding: utf-8 -*-
"""
Topic: 使用splash爬取动态页面
"""
import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest


class UsesplashspiderSpider(scrapy.Spider):
    name = 'useSplashSpider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        for url in self.start_urls:
            # 两种方法都可以达到同样的效果
            yield SplashRequest(url, self.parse, args={'wait': 0.5})
            yield scrapy.Request(url, self.parse, meta={'splash': {'wait': 0.5}})

    def parse(self, response):
        # meta['splash']['args'] 包含了发往Splash的参数。
        # meta['splash']['endpoint'] 指定了Splash所使用的endpoint，默认是render.html
        # meta['splash']['splash_url'] 覆盖了settings.py文件中配置的Splash URL
        # meta['splash']['splash_headers'] 运行你增加或修改发往Splash服务器的HTTP头部信息，注意这个不是修改发往远程web站点的HTTP头部
        # meta['splash']['dont_send_headers'] 如果你不想传递headers给Splash，将它设置成True
        # meta['splash']['slot_policy'] 让你自定义Splash请求的同步设置
        # meta['splash']['dont_process_response'] 当你设置成True后，SplashMiddleware不会修改默认的scrapy.Response请求.
        # 默认是会返回SplashResponse子类响应比如SplashTextResponse
        # meta['splash']['magic_response'] 默认为True，Splash会自动设置Response的一些属性，比如response.headers, response.body等

        # SplashFormRequest使用
        yield SplashFormRequest(response.url, self.next_parse, formdata={'name': '111'})

    def next_parse(self, response):
        # SplashResponse
        # 二进制响应，比如对 / render.png的响应
        # SplashTextResponse
        # 文本响应，比如对 / render.html的响应
        # SplashJsonResponse
        # JSON响应，比如对 / render.json或使用Lua脚本的 / execute的响应
        # 留3个response类型坑, scrapy-splash在docker运行起来后并没有操作难度,示例略过
        pass
