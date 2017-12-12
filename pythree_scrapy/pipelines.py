# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import copy

from twisted.enterprise import adbapi
from datetime import datetime
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem


class StudyscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLChyxxPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        copyItem = copy.deepcopy(item)
        d = self.dbpool.runInteraction(self._do_insert, copyItem, spider)
        d.addBoth(lambda _: item)
        return d

    def _do_insert(self, conn, item, spider):
        sql = """
            insert into ifeng_news(title, content, url, time, news_from, news_type, )
            values(%s, %s, %s, %s, %s, %s, %s)
        """
        conn.execute(sql, (item['title'], item['content'], item['url'], item['time'], item['news_from'], item['news_type']))


class MyFilePipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        # 修改这个方法可以在pipeline中修改文件保存路径
        item = request.meta['item']
        return item['file_paths']

    def get_media_requests(self, item, info):
        # 返回一个Request对象
        for file_url in item['file_urls']:
            yield Request(file_url)

    def item_completed(self, results, item, info):
        # 当Request下载完成后,填充files字段
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no file")
        item['file_paths'] = file_paths
        return item
