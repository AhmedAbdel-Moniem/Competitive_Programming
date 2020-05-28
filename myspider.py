import scrapy

class Scraper(scrapy.Spider):
	name = "quotes"
	def start_requests(self):
		urls = ['https://www.alishahin.net/']
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('saved file %s' % filename)