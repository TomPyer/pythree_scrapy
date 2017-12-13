# pythree_scrapy
python3 study test..

有过一段时间的scrapy使用,但是仅停留在知其然不知其所以然层面
现在有空,专门开个项目记录逐步学习的过程.

关键字:python3, scrapy, scrapyd

部分代码用到之前项目copy的内容,有重新理解和修改部分

从基础的scrapy项目逐步深入,过程可由push日志观察

因为之前一直使用py2.7,部分urllib库操作尚未完全记住,所以列出：

在Pytho2.x中使用import urllib2——-对应的，在Python3.x中会使用import urllib.request，urllib.error。

在Pytho2.x中使用import urllib——-对应的，在Python3.x中会使用import urllib.request，urllib.error，urllib.parse。

在Pytho2.x中使用import urlparse——-对应的，在Python3.x中会使用import urllib.parse。

在Pytho2.x中使用import urlopen——-对应的，在Python3.x中会使用import urllib.request.urlopen。

在Pytho2.x中使用import urlencode——-对应的，在Python3.x中会使用import urllib.parse.urlencode。

在Pytho2.x中使用import urllib.quote——-对应的，在Python3.x中会使用import urllib.request.quote。

在Pytho2.x中使用cookielib.CookieJar——-对应的，在Python3.x中会使用http.CookieJar。

在Pytho2.x中使用urllib2.Request——-对应的，在Python3.x中会使用urllib.request.Request


以及 urllib.parse.encode(data) 报错: 
  TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
使用urllib.parse.encode(data).encode(encoding="UTF8") 解决
* 问题来由详见关于 curlApi/main.py 内


更新预告：
   简书：http://www.jianshu.com/p/75d26f00ddb1 关于docker的安装和使用（windows下）
   
   简书：http://www.jianshu.com/p/dffa49ea48c3 关于scrapy-splash的安装和使用（同上）


更新个问题...

    由于本地py27和36的共存问题,不胜其烦,然后卸载了py27,卸载后重新安装scrapyd等模块,结果导致scrapyd启动后无法读取spiders
