import scrapy


class AromadbSpider(scrapy.Spider):
    name = 'aromadb'
    
    start_urls = ['http://bioinfo.cimap.res.in/aromadb/web_search_plant.php']

    def parse(self, response):
        for resp in response.xpath('//*[@id="myTable"]/tbody/tr'):
            yield{
                'link':'http://bioinfo.cimap.res.in/aromadb/'+resp.xpath('./td[5]/a/@href').get()
            }
       