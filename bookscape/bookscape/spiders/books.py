from datetime import datetime

from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule


class Books(CrawlSpider):
    name = "books"
    start_urls = ["https://books.toscrape.com"]
    rules = [
        Rule(
            LinkExtractor(restrict_css="article.product_pod"),
            callback="parse_items"
        )
    ]

    def parse(self, response: Response, **_kwargs):
        pass

    def parse_items(self, response: Response):
        name = response.css("div.col-sm-6.product_main h1::text").get()
        description = response.css("div#product_description + p::text").get()
        trs = response.css("table.table.table-striped tr")

        tmp = {
            "spider_name": self.name,
            "datetime_scraped": datetime.now().strftime("%Y-%m-%d"),
            "name": name,
            "description": description
        }

        for tr in trs:
            col_name = tr.css("th::text").get()
            col_value = tr.css("td::text").get()

            tmp[col_name] = col_value
