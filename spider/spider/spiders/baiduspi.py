import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    start_urls = [
        "http://www.baidu.com"
    ]

    def parse(self, response):
        filename = "bdcom.html"
        with open(filename, 'wb') as f:
            f.write(response.body)