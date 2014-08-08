#coding=utf8
import scrapy
from spider.items import DmozItem
from datahandle import AirData

class BingSpider(scrapy.Spider):
    def start_requests(self):
        # cityname1=u'上海'
        # cityname2=u'广州'
        # cityname1=cityname1.encode('gb2312')
        # cityname2=cityname2.encode('gb2312')
        a=AirData()
        datas=a.UsaData()
        for info1 in datas:
            for info2 in datas:
                if (info1!=info2):
                    print (info1)

                    formdata={
                    'cond.tripType':'OW',
                    'cond.depCode_reveal':info1['code'],
                    'cond.depCode':info1['code'],
                    'cond.arrCode_reveal':info2['code'],
                    'cond.arrCode':info2['code'],
                    'cond.routeType':'3',
                    'depDate':'2014-07-29',
                    'depRtData':'2014-8-26',
                    }
                    print('========================================')
                    print (formdata)
                    yield scrapy.FormRequest("http://www.bing.com/flights/search",
                                    formdata=formdata,
                                    callback=self.logged_in,
                                    dont_filter=True)

    def logged_in(self, response):
        print 1
        print response.url
        for sel in response.xpath('//body'):
            item = DmozItem()
            item['price']=sel.xpath('//b').extract()
            yield item
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
    name = "bing"
    allowed_domains = ["www.bing.com"]
    # start_urls = [
    #     "http://flights.ctrip.com/"
    # ]

    # def parse(self, response):
    #     for sel in response.xpath('//body'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()

    #         print sel.xpath('')
    #         # for m in desc:
    #         #     m=m.decode('utf8')
    #         yield item