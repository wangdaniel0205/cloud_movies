import scrapy

#scrapy crawl fmovies -o items.json
'''
class QuoteSpider(scrapy.Spider):
    name = "fmovies"
    start_urls = [
        "https://fmovies.to/movies?page=1"
    ]

    def parse(self, response):
        href = response.css('.poster::attr(href)').extract()
        yield {
            'links': href
        }
'''
class QuoteSpider(scrapy.Spider):
    name = "fmovies"
    start_urls = [
        "https://fmovies.to/film/the-house-of-flowers-the-movie.qn55v"
    ]

    def parse(self, response):
        title = response.css('.title::text').extract()
        yield {
            'title': title
        }