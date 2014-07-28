import scrapy

class DmozSpider(scrapy.Spider):
    name = "qne"
    DOWNLOAD_DELAY=10
    #allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://flight.qunar.com/site/roundtrip_list_new.htm?fromCity=%E4%B8%8A%E6%B5%B7&toCity=%E5%8C%97%E4%BA%AC&fromDate=2014-07-30&toDate=2014-08-02&from=qunarindex'
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)