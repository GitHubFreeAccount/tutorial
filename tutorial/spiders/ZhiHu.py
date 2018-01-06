# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import scrapy
import re
from scrapy.spider import CrawlSpider
from scrapy import Selector
from tutorial.items import DmozItem

class Douban(CrawlSpider):
    name = "douban"
    allowed_domains = ["zhihu.com"]
    start_urls=[
        # 'https://www.resource-zone.com/'
        # ,
       'https://www.zhihu.com/question/53369195/answer/287018565'
    ]

    def parse(self, response):
        # chapther 1 css
        # print response.body
        # print response.css('meta::attr(content)')[0].extract()
        #CSS 伪元素 (Pseudo-elements)
        # for jscript in response.css('script::text'):
        #     print jscript.extract()
        #
        # for metalabel in response.css('meta::attr(content)'):
        #     print metalabel.extract()

        #chapter 2 selecter  xpath
        # sel=Selector(text=response.body,type="html")
        # for labelp in sel.xpath('//div[@class="RichContent-inner"]/span/p/text()'):
        #     print labelp.extract().encode('utf-8')



        # for labela in sel.xpath('//a'):
        #     item=DmozItem()
        #     item['title']=labela.xpath('@class').extract()
        #     item['link']=labela.xpath('@href').extract()
        #     yield item

        #使用beautifulSoup解析html
        soup=BeautifulSoup(response.body,"lxml")
        # print soup.body.a #获取第一个tag

        # print soup.body.a.contents[0].name

         #获取所有a标签
        # for lablesvg in  soup.find_all('svg'):
        #     print lablesvg;
        # print  soup.p.string
        # print type(soup.p.string)
        # for labelp in soup.find_all('p'):
        #     print labelp.string
            # for str in labelp.stripped_strings:
            #     print str
        # BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name
        # print soup.name

        #find_all
        # print soup.find_all('img')[0]['src']
        # print soup.find_all(role='navigation')[0].a
        # print soup.find_all(role='navigation')[0].a.attrs
        # print soup.find_all(role='navigation')[0].a['class']
        # print soup.find_all(role='navigation')[0].a.string

        #rules
        for img in soup.find_all('img'):
            item=DmozItem()
            item['link']=img['src']
            yield item
        for url in response.xpath('//a/@href').extract():
             if(url.find('http')==-1):
                 url= 'https://www.zhihu.com'+url
             yield scrapy.Request(url, callback=self.parse)