from datetime import date
from pprint import pprint
from bs4 import BeautifulSoup
import requests

class Scraper:
	
	@classmethod
	#Utilizes BeautifulSoup to simulate request from a browser, then allows us to scrape the webpage as a browser would see it (with javascript, css, etc.) so that we can correctly extract dynamically generated data

	def amazonScrape(self, url, product_code):
		
		product_url = url+product_code
		response = requests.get(product_url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

		soup = BeautifulSoup(response.content)

		for li in soup.select('span#productTitle'):
		    try:
			itemTitle = li.getText().strip()

		    except AttributeError:
			break

		for li in soup.select('span#priceblock_ourprice'):
		    try:
			price = li.getText()

		    except AttributeError:
			break

		#Returns list of item titles (1 in our case)	
		
		print "Title: ", itemTitle

		
		print "Price: ", price

		#implicit check for null variable
		if price:

			#Outputs a dictionary with key value pairs for item name and prices of the item, as well as date of the scrape	
			yyyymmdd = date.today().strftime("%Y%m%d")

			price_collection = dict()
			price_collection[yyyymmdd] = price

			return dict(name=itemTitle, price_history=price_collection)

		#Else possible invalid product code.
		else:
			print "Error: item not able to be scraped. Please make sure that your product code is valid and is entered correctly\n"
			return -1
