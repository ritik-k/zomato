# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZomatoItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    names = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    location = scrapy.Field()
    cost = scrapy.Field()
    cuisine = scrapy.Field()
    featured = scrapy.Field()
    urls = scrapy.Field()
    
class ZlocItem(scrapy.Item):
    location = scrapy.Field()
    names = scrapy.Field()