import scrapy
import pandas as pd


class AromadetailsSpider(scrapy.Spider):
    name = "aromadetails"
    allowed_domains = ["bioinfo.cimap.res.in"]
    # start_urls = ["http://bioinfo.cimap.res.in/"]
    data = pd.read_csv("aromadblink.csv")
    url = data["link"].to_list()

    start_urls = url

    def parse(self, response):
        yield {
            "Scientific Name": response.xpath(
                '//*[@id="divchallan"]/div[2]/div[1]/div[4]/i/text()'
            ).get(),
            "Introduction": response.xpath(
                '//*[@id="divchallan"]/div[3]/div/div[2]/p/text()'
            ).get(),
            "Details": response.xpath(
                '//*[@id="divchallan"]/div[3]/div/div[4]/text()/text()'
            ).get(),
            "Essential Oil Name": response.xpath(
                '//*[@id="divchallan"]/div[4]/div/table/tbody/tr/td[2]/a/text()'
            ).get(),
            "Essential Oil Link": "http://bioinfo.cimap.res.in/aromadb/"
            + response.xpath(
                '//*[@id="divchallan"]/div[4]/div/table/tbody/tr/td[2]/a/@href'
            ).get(),
        }
