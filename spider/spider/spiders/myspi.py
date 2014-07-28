#coding=utf8
import scrapy
from spider.items import DmozItem
class DmozSpider(scrapy.Spider):
    def start_requests(self):
        # cityname1=u'上海'
        # cityname2=u'广州'
        # cityname1=cityname1.encode('gb2312')
        # cityname2=cityname2.encode('gb2312')
        formdata={
        'cond.tripType':'OW',
        'cond.depCode_reveal':'JFK',
        'cond.depCode':'JFK',
        'cond.arrCode_reveal':'BHY',
        'cond.arrCode':'BHY',
        'cond.routeType':'3',
        'depDate':'2014-07-29',
        'depRtData':'2014-8-26',
        }
        return [scrapy.FormRequest("http://us.ceair.com/muovc/front/reservation/flight-search!doFlightSearch.shtml",
                               formdata=formdata,
                               callback=self.logged_in)]

    def logged_in(self, response):
        print 1
        print response.url
        from scrapy.shell import inspect_response
        inspect_response(response)
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass
    name = "dmoz"
    # allowed_domains = ["flights.ctrip.com"]
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