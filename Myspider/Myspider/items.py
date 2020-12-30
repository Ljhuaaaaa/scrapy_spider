# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    pic_href1 = scrapy.Field()
    pic_href2 = scrapy.Field()
    info_href = scrapy.Field()
    details = scrapy.Field()
    product_class = scrapy.Field()
    grain = scrapy.Field()
    norms = scrapy.Field()
    glaze = scrapy.Field()
    scene = scrapy.Field()
    patent = scrapy.Field()
    identify = scrapy.Field()
    features = scrapy.Field()
    space = scrapy.Field()
