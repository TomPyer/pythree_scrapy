#! coding: utf-8
"""
Topic: 动态配置爬虫-脚本启动多爬虫
"""

import logging
from dynamicSpider.articleSpider import ArticleSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from dynamicSpider.models import db_connect
from dynamicSpider.models import ArticleRule
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    settings = get_project_settings()
    configure_logging(settings)
    db = db_connect()
    Session = sessionmaker(bind=db)
    session = Session()
    rules = session.query(ArticleRule).filter(ArticleRule.enable == 1).all()
    session.close()
    runner = CrawlerRunner(settings)

    for rule in rules:
        # stop reactor when spider closes
        # runner.signals.connect(spider_closing, signal=signals.spider_closed)
        runner.crawl(ArticleSpider, rule=rule)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    # blocks process so always keep as the last statement
    reactor.run()
    logging.info('all finished.')


