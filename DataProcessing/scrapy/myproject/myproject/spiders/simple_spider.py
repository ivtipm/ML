import scrapy

class SimpleSpider(scrapy.Spider):
    name = "simple"                  # имя паука
    start_urls = ["https://quotes.toscrape.com/"]  # сайт для примера

    def parse(self, response):
        # собираем все цитаты на странице
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }
