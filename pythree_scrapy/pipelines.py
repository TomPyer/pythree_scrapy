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
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = """
            insert into gdhf_data(title, content, url, date, insert_time)
            values(%s, %s, %s, %s, %s)
        """
        conn.execute(sql, (item['title'], item['content'], item['url'], item['date'], now))


class MyFilePipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        return item['file_paths']

    def get_media_requests(self, item, info):
        # for file_url in item['file_urls']:
        yield Request(item['file_urls'], meta={'item': item})

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no file")
        # item['file_paths'] = file_paths
        return item
