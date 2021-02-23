import scrapy

from tutorail.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['https://www.agefans.net/']
    start_urls = [
        'https://www.agefans.net/rank'
        ]

    def parse(self,response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="blockcontent div_right_r_3"]/ul/li')
        items = []
        for site in sites:
            item= DmozItem()
            item['title'] = site.xpath('span/text()').extract()
            item['desc'] = site.xpath('a/span/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            
            items.append(item)

        return items

    
        
    
