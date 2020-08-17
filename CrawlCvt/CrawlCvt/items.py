# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlcvtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    acronyms = scrapy.Field()
    vietnamese = scrapy.Field()
    english = scrapy.Field()