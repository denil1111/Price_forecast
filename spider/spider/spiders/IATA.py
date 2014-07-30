import scrapy
from spider.items import DmozItem

class IateSpider(scrapy.Spider):
    name = "iata"
    start_urls = [
        "http://airportcode.51240.com/",
        "http://airportcode.51240.com/2__airportcode/"
    ]
    for i in range(3,290):
        start_urls.append("http://airportcode.51240.com/"+str(i)+"__airportcode/")
    def parse(self, response):
        item = DmozItem()
        tf=0
        for sel in response.xpath('//tr'):
            item['name']=sel.xpath('td/a/text()').extract()
            item['desc']=sel.xpath('td/text()').extract()
            yield item