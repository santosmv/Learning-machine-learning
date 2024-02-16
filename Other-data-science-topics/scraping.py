from scrapy import Spider

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

# To run: scrapy runspider scraping.py
# To save in a file: scrapy runspider scraping.py -O scraped.json