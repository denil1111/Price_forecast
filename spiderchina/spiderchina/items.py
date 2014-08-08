import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    date= scrapy.Field()