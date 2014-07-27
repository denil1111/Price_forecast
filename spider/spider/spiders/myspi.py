import scrapy
from spider.items import DmozItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.baidu.com"
    ]

    def parse(self, response):
        for sel in response.xpath('//a'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            # for m in desc:
            #     m=m.decode('utf8')
            yield item