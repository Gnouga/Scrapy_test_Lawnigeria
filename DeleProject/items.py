# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted Data - > Temporary containers (items) - > Storing in database

import scrapy

class DeleprojectItem(scrapy.Item):
    content = scrapy.Field()
    url = scrapy.Field()

