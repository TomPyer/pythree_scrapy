# -*- coding: utf-8 -*-

# Scrapy settings for pythree_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pythree_scrapy'

SPIDER_MODULES = ['pythree_scrapy.spiders']
NEWSPIDER_MODULE = 'pythree_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pythree_scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pythree_scrapy.middlewares.PythreeScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pythree_scrapy.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pythree_scrapy.pipelines.MySQLChyxxPipeline': 300,      # 启用存入数据库的pipeline
   # 'pythree_scrapy.pipelines.MyFilePipeline': 301,         # 启用文件下载pipeline
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'scrapy.pipelines.files.FilesPipeline': 2,
}

FILES_STORE = '/path/to/valid/dir'   # 文件存储路径
IMAGES_STORE = '/path/to/valid/dir'  # 图片存储路径
# 90 days of delay for files expiration
FILES_EXPIRES = 90
# 30 days of delay for images expiration
IMAGES_EXPIRES = 30
# 图片缩略图
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
# 图片过滤器，最小高度和宽度
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Mysql Setting
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'testDB'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''

DATABASE = {'drivername': 'mysql',
            'host': '127.0.0.1',
            'port': '3306',
            'username': 'root',
            'password': '******',
            'database': 'test',
            'query': {'charset': 'utf8'}}

# 分布式爬虫概念
# Scrapy并没有提供内置的分布式抓取功能，不过有很多方法可以帮你实现。
# 如果你有很多个spider，最简单的方式就是启动多个Scrapyd实例，然后将spider分布到各个机器上面。
# 如果你想多个机器运行同一个spider，可以将url分片后交给每个机器上面的spider。比如你把URL分成3份
# 主爬虫获取url存入redis, 再由不同的scrapyd实例从redis中获取url进行爬取,达到分布式效果

# 防封策略
# 使用user agent池。也就是每次发送的时候随机从池中选择不一样的浏览器头信息，防止暴露爬虫身份
# 禁止Cookie，某些网站会通过Cookie识别用户身份，禁用后使得服务器无法识别爬虫轨迹
# 设置download_delay下载延迟，数字设置为5秒，越大越安全
# 如果有可能的话尽量使用Google cache获取网页，而不是直接访问
# 使用一个轮转IP池，例如免费的Tor project或者是付费的ProxyMesh
# 使用大型分布式下载器，这样就能完全避免被封了，只需要关注怎样解析页面就行。一个例子就是Crawlera

# 防止被Ban的策略设置
DOWNLOAD_TIMEOUT = 20
DOWNLOAD_DELAY = 5
# 禁用Cookie
COOKIES_ENABLES = True

# 日志设置
import logging
LOG_LEVEL = logging.INFO
LOG_STDOUT = True
LOG_FILE = "E:/logs/spider.log"
LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
