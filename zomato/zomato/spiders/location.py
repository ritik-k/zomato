import scrapy
from ..items import ZlocItem

class Zloc(scrapy.Spider):
    name = 'loc_r'
    with open('/home/ritik/data73/zomato/urls.csv') as f:
        start_urls = f.readlines()
        
    def parse(self, response):
        
        items = ZlocItem()
        
        location = response.css('a[rel="noopener noreferrer"]::attr(href)').extract_first()
        names = response.css('h1::text').extract_first()
        items['location'] = location
        items['names']=names
        yield items
    
    
