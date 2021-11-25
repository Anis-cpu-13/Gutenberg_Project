import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import CsvItemExporter
    
        
class GutenbergSpider(scrapy.Spider):
    name = "gutenberg"
    start_urls = [
        'https://www.gutenberg.org/browse/scores/top#books-last30',    
    ]

    def parse(self, response):

        for result in response.css('div.padded > ul > li > a'):
            yield response.follow(url=result.xpath('@href').extract_first(), callback=self.parse_detail)
        
        
   
    def parse_detail(self, response):
        author = response.css('parse_detail::text').get()

        yield {
            'author' : author.strip()
        }
process = CrawlerProcess (
    {'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '}
)

process.crawl(GutenbergSpider)
process.stop()
process.start()