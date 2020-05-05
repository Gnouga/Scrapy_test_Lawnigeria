import scrapy
from ..items import DeleprojectItem

class DeleSpider(scrapy.Spider):

    name='Lawnigeria'
    start_urls=[
        'https://lawnigeria.com/2018/06/3plr-banking-and-finance/'
    ]

    def parse(self, response):

        items = DeleprojectItem() # instance
        para = response.css('tr+ tr a::text')[0].extract()
        link= response.css('tr+ tr td a').xpath('@href')[0].extract()
        items['content']=para
        items['url'] = link
        yield items
