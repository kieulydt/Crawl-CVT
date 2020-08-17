# -*- coding: utf8 -*-
import scrapy
from CrawlCvt.items import CrawlcvtItem
from html import unescape
from w3lib.html import replace_entities


class CvtSpider(scrapy.Spider):
    name = 'cvt'
    allowed_domains = ['chuviettat.com']
    start_urls = ['http://chuviettat.com/']
    domain = 'http://chuviettat.com/cvts/search/'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_alpha)

    def parse_alpha(self, response):
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for character in alpha:
            url = self.domain + character + '/'
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        url = response.url
        all_page = response.css('div.pagination span.number a::text').getall()
        total_page = int(all_page[-3]) +1
        for i in range(total_page):
            page = str(i+1)
            new_url = url + 'page:' + page
            yield scrapy.Request(url=new_url, callback=self.parse_item)

    def parse_item(self, response):
        try:
            record = CrawlcvtItem()
            for item in response.css('table.table-striped tr'):
                x = item.css('td::text').getall()
                if(x[1].strip()!= 'Chữ tắt'):
                    record['acronyms'] = x[1].strip()
                    record['vietnamese'] = x[2].strip()
                    record['english'] = x[3].strip()
                    record['acronyms'] = replace_entities(unescape(record['acronyms']))
                    record['vietnamese'] = replace_entities(unescape(record['vietnamese']))
                    yield record
        except:
            print("error")

