from datetime import date
from lxml import html
import requests

class Scraper:
	
	def amazonScrape(url, product_code)
		
		webpage = requests.get(url+product_code)
		html_tree = html.fromstring(webpage.content)

		#Returns list of item titles (1 in our case)	
		itemTitles = html_tree.xpath('//span[@id="productTitle"]/text()')

		#Returns list of item prices (1 in our case)
		prices = html_tree.xpath('//span[@id="priceblock_ourprice"]/text()')

		#Outputs a dictionary with key value pairs for item name and prices of the item, as well as date of the scrape	
		price_collection = dict(date.today()=prices.pop())
		return dict(name=itemTitles.pop(), prices=price_collection)
