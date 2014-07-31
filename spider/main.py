from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
# from spider.spiders.baiduspi import BaiduSpider
from spider.spiders.myspi import DmozSpider
from scrapy.utils.project import get_project_settings
from spider.items import DmozItem

spider = DmozSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run()
item=DmozItem()
print item
print 1