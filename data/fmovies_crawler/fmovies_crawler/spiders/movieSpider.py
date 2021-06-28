import scrapy

#scrapy crawl fmovies -o items.json

base_url = 'https://fmovies.to'
num_page = 2



class QuoteSpider(scrapy.Spider):
    name = "fmovies"
    start_urls = [base_url+'/movies?page={}'.format(i) for i in range(1, 1+num_page)]
    current_id = 1

    def parse(self, response):
        # get single movie links
        hrefs = response.css('.poster::attr(href)').extract()

        for href in hrefs:
            next_link = base_url+href
            yield response.follow(next_link, callback=self.get_movie_info)


    def get_movie_info(self, response):
        yield {
            'id': self.get_id(),
            'title': response.css('h1.title::text').extract()[0],
            'rating': response.css('.imdb::text').extract()[0][1:],
            'length': response.css('.imdb+span::text').extract()[0],
            'description': response.css('.desc::text').extract()[0][1:],
            'country': response.css('.meta div:nth-child(1) a::text').extract()[0],
            'genre': response.css('.meta div:nth-child(2) a::text').extract(),
            'release': response.css('.meta div:nth-child(3) span+span::text').extract()[0],
            'director': response.css('.meta div:nth-child(4) span+span::text').extract(),
            'cast': response.css('.shorting span::text').extract(),
            'image_src': response.css('img::attr(src)').extract()[0]
        }

    def get_id(self):
        id = (5-len(str(self.current_id))) * '0' + str(self.current_id)
        self.current_id += 1
        return id