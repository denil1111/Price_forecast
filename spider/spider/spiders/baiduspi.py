import scrapy
from spider.items import DmozItem
from datahandle import AirData
class kawSpider(scrapy.Spider):
    name = "kaw"
    DOWNLOAD_DELAY = 2
    # start_urls=[]
    def start_requests(self):
        a=AirData()
        datas=a.UsaData()

        # start_urls.append('http://www.kayak.com/flights/'+datas[1]['code']+'-'+datas[2]['code']+'/2014-08-26')    
        # start_urls.append('http://www.kayak.com/flights/'+datas[1]['code']+'-'+datas[3]['code']+'/2014-08-26')    
        for i in range(25,27):
            date='/2014-08-'+str(i)
            if (i==32):
                date='/2014-09-01'
            for info1 in datas:
                for info2 in datas:
                    if (info1!=info2):
                        yield scrapy.FormRequest('http://www.kayak.com/flights/'+info1['code']+'-'+info2['code']+date,
                                                callback=self.ress
                                            )
                    
                    # print start_urls
                    # start_urls.append('http://www.kayak.com/flights/'+info1['code']+'-'+info2['code']+'/2014-08-26')     
    def ress(self, response):
        filename = "bdcom.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        item = DmozItem()
        tf=0
        for sel in response.xpath('/*'):
            item['price']=sel.xpath('//a[@class="bestPrice"]/text()').extract()
            item['name']=response.url[29:36]
            item['date']=response.url[37:]
            print sel.xpath('//a[@class="bestPrice"]/text()').extract()
            print (item);
            yield item