import scrapy
from ..items import ZomatoItem

class Zomato(scrapy.Spider):
    name = 'all_r'
    page_no = 2
    start_urls = ['https://www.zomato.com/mumbai/best-restaurants?page=1']
    
    def parse(self, response):
        
        items = ZomatoItem()
        
        all_div_r = response.css('div.search-snippet-card')
        
        for r in all_div_r:
            
            category = r.css('a.fontsize6::text').extract()
            names = r.css('a.fontsize0::text').extract()
            rating = r.css('span.rating-value::text').extract()
            reviews = r.css('span.rating-div:nth-child(1) .medium , .single-rating .medium::text').extract()
            location = r.css("b::text").extract()
            cost = r.css('div.res-cost .pl0::text').extract()
            cuisine = r.css('.nowrap a::text').extract()
            featured = r.css('.search-grid-right-text a::text').extract()
            urls = r.css('a.fontsize0::attr(href)').get()
            
            items['category'] = category
            items['names'] = names
            items['rating'] = rating
            items['reviews'] = reviews
            items['location'] = location
            items['cost'] = cost
            items['cuisine'] = cuisine
            items['featured'] = featured
            items['urls'] = urls
            
            yield items
            
        next_page = 'https://www.zomato.com/mumbai/best-restaurants?page=' + str(Zomato.page_no)
        
        if Zomato.page_no <= 70:
            Zomato.page_no += 1
            yield response.follow(next_page, callback=self.parse)
            
            
            