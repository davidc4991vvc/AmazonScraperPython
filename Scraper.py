from datetime import date
from pprint import pprint
from bs4 import BeautifulSoup
import requests

class Scraper:
	
	@classmethod
	def amazonScrape(self, url, product_code):
		
		product_url = url+product_code
		response = requests.get(product_url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

		soup = BeautifulSoup(response.content)
		tags = {}
		for li in soup.select('span#productTitle'):
		    try:
			itemTitle = li.getText().strip()
			#key = title.text.strip().rstrip(':')
			#value = title.next_sibling.strip()

		    except AttributeError:
			break

		for li in soup.select('span#priceblock_ourprice'):
		    try:
			price = li.getText()
			#key = title.text.strip().rstrip(':')
			#value = title.next_sibling.strip()

		    except AttributeError:
			break

		#Returns list of item titles (1 in our case)	
		
		print "Title: ", itemTitle

		
		print "Price: ", price

		#implicit check for null with python magic
		if price:

			#Outputs a dictionary with key value pairs for item name and prices of the item, as well as date of the scrape	
			yyyymmdd = date.today().strftime("%Y%m%d")
			print "date: ", yyyymmdd

			price_collection = dict()
			price_collection[yyyymmdd] = price

			return dict(name=itemTitle, price_history=price_collection)

		else:
			print "Item not able to be scraped. Exiting..."
			exit(1)

