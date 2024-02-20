from scrapy import Spider, Request

class Collect(Spider):
    name = 'OurCollector'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("*//div[@class='quote']")
        for q in quotes:
            yield {
                'title':q.xpath(".//span[@class='text']/text()").get(),
                'author':q.xpath(".//small[@class='author']/text()").get(),
                'tags':q.xpath(".//div[@class='tags']/a[class='tag']/text()").getall()
            }
        
        next_page = response.xpath("*//li[@class='next']/a/@href").get()

        if next_page is not None:
            join = response.urljoin(next_page)
            yield Request(join, callback=self.parse)

# To run: scrapy runspider scraping.py
# To save in a file: scrapy runspider scraping.py -O scraped.json