from Item import Item
from MongoDBHelper import MongoDBHelper
from Scraper import Scraper
import time

print "Amazon Scraper: Where all your frugal dreams come true.\n"

url = "http://www.amazon.com/gp/product/"

database = MongoDBHelper.setupDB()

cursor = database.items.find()

if cursor.count() > 0:
	for document in cursor:
		print "Updating price data for the day... please wait...\n"
		temp_product_code = document['product_code']
		updateScrape = Scraper.amazonScrape(url, temp_product_code)
		
		#If scraping successful, update data for current item, else continue
		if updateScrape != -1:

			tempItem = Item(updateScrape['name'], updateScrape['price_history'], temp_product_code)
			MongoDBHelper.updatePriceHistory(tempItem, database)

		time.sleep(60)

choice = 0

while choice != 4:
	print "1. Define new item\n"
	print "2. Check current items\n"
	print "3. Delete an item\n"
	print "4. Exit\n"

	choice = raw_input("Please select an option by entering a number, 1 through 4 :")

	try:
		choice = int(choice)
	except ValueError:
		print "Error: input not numeric. Please try again!\n"
		continue

	if (choice < 0) or (choice > 4):
		print "Error: choice not defined. Please try again!\n"

	elif choice == 1:
		print "Define new item\n"
		 #define new item here
		prod_code = raw_input("Please enter the Amazon.com product code string for your item: ")
	
		newScrape = Scraper.amazonScrape(url, prod_code)

		if newScrape != -1:

			newItem = Item(newScrape['name'], newScrape['price_history'], prod_code)
			MongoDBHelper.addItem(newItem, database)
		else:
			print "Item not found. Please try again.\n"

     	elif choice == 2:
		print "View all items\n"
		 #view items here

		MongoDBHelper.viewAllItems(database)

	elif choice == 3:
		print "Delete an item\n"
		 #delete an item here

		prod_code = raw_input("Please enter the Amazon.com product code string for your item: ")
		MongoDBHelper.deleteItem(prod_code, database)
	else:
		print "Exiting now..."

