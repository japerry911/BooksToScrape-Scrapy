from datetime import datetime

from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders.crawl import CrawlSpider, Rule

from bookscape.items import BookItem


class Books(CrawlSpider):
    name = "books"
    start_urls = ["https://books.toscrape.com"]
    rules = [
        Rule(
            LinkExtractor(restrict_css="article.product_pod"),
            callback="parse_items"
        )
    ]
    product_info_names = {
        "UPC": "upc",
        "Product Type": "product_type",
        "Price (excl. tax)": "price_excl_tax",
        "Price (incl. tax)": "price_incl_tax",
        "Tax": "tax",
        "Availability": "availability",
        "Number of Reviews": "number_of_reviews"
    }

    def parse(self, response: Response, **_kwargs):
        pass

    def parse_items(self, response: Response):
        loader = ItemLoader(
            item=BookItem(),
            selector=response
        )

        loader.add_value("spider_name", self.name)
        loader.add_value(
            "datetime_scraped",
            datetime.now().strftime("%Y-%m-%d")
        )
        loader.add_css(
            "name",
            "div.col-sm-6.product_main h1::text"
        )
        loader.add_css(
            "description",
            "div#product_description + p::text"
        )

        trs = response.css("table.table.table-striped tr")
        for tr in trs:
            col_name = tr.css("th::text").get()
            col_value = tr.css("td::text").get()

            if col_name in self.product_info_names:
                loader.add_value(
                    self.product_info_names[col_name],
                    col_value
                )
            else:
                print(
                    f"---ALERT---\n\t{col_name} not in product_info_names"
                )

        return loader.load_item()
