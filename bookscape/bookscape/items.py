from itemloaders.processors import TakeFirst
from scrapy import Field, Item


class BookItem(Item):
    spider_name = Field(
        output_processor=TakeFirst()
    )
    datetime_scraped = Field(
        output_processor=TakeFirst()
    )
    name = Field(
        output_processor=TakeFirst()
    )
    description = Field(
        output_processor=TakeFirst()
    )
    upc = Field(
        output_processor=TakeFirst()
    )
    product_type = Field(
        output_processor=TakeFirst()
    )
    price_excl_tax = Field(
        output_processor=TakeFirst()
    )
    price_incl_tax = Field(
        output_processor=TakeFirst()
    )
    tax = Field(
        output_processor=TakeFirst()
    )
    availability = Field(
        output_processor=TakeFirst()
    )
    number_of_reviews = Field(
        output_processor=TakeFirst()
    )
