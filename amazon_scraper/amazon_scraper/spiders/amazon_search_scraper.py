import scrapy

base_url = "http://www.amazon.com"


class Scraper(scrapy.Spider):
    name = "amazon_search"

    def init(self, keyword):

        self.keyword = keyword.replace(' ', '+')

        start_urls = [

        ]
