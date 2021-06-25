import scrapy

#scrapy crawl fmovies -o items.json

'''
class QuoteSpider(scrapy.Spider):
    name = "fmovies"
    start_urls = [
        "https://fmovies.to/film/the-house-of-flowers-the-movie.qn55v"
    ]

    def parse(self, response):

        yield {
            'name': response.css('h1.title::text').extract(),
            'rating': [response.css('.imdb::text').extract()[0]],
            'length': response.css('.imdb+span::text').extract(),
            'description': [response.css('.desc::text').extract()[0]],
            'country': response.css('.meta div:nth-child(1) a::text').extract(),
            'genre': response.css('.meta div:nth-child(2) a::text').extract(),
            'release': response.css('.meta div:nth-child(3) span+span::text').extract(),
            'director': response.css('.meta div:nth-child(4) span+span::text').extract(),
            'cast': response.css('.shorting span::text').extract(),
            'image_src': [response.css('img::attr(src)').extract()[0]]
        }
'''

base_url = 'https://fmovies.to'
num_page = 2

class QuoteSpider(scrapy.Spider):
    name = "fmovies"
    start_urls = [base_url+'/movies?page={}'.format(i) for i in range(1, 1+num_page)]

    def parse(self, response):
        # get single movie links
        hrefs = response.css('.poster::attr(href)').extract()

        for href in hrefs:
            next_link = base_url+href
            yield response.follow(next_link, callback=self.get_movie_info)


    def get_movie_info(self, response):
        yield {
            'title': response.css('h1.title::text').extract(),
            'rating': [response.css('.imdb::text').extract()[0]],
            'length': response.css('.imdb+span::text').extract(),
            'description': [response.css('.desc::text').extract()[0]],
            'country': response.css('.meta div:nth-child(1) a::text').extract(),
            'genre': response.css('.meta div:nth-child(2) a::text').extract(),
            'release': response.css('.meta div:nth-child(3) span+span::text').extract(),
            'director': response.css('.meta div:nth-child(4) span+span::text').extract(),
            'cast': response.css('.shorting span::text').extract(),
            'image_src': [response.css('img::attr(src)').extract()[0]]
        }