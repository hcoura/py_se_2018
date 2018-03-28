# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['http://localhost:8000/wikipedia/Clube_Atlético_Mineiro.html']

    def parse(self, response):
        image = response.css('.mw-parser-output table img::attr(src)').extract_first()
        title = response.css('#firstHeading::text').extract_first()
        related = response.xpath('//div[@id="bodyContent"]/descendant::a[re:test('
                                 '@href, "^[^:]*\.html$")]/@href').extract()[:5]
        paragraph = ''.join(response.xpath('//div[@class="mw-parser-output"]/p[1]/'
                                           'descendant-or-self::*[self::a[not(starts-with(@href,'
                                           ' "#cite"))] or self::b or self::p]/text()').extract())

        yield {
            'title': title,
            'image': image,
            'paragraph': paragraph,
            'related_articles': related,
        }
