from pymongo import MongoClient
from Item import Item
from datetime import date

class MongoDBHelper:
	
	@classmethod
	#Setup DB client and returns relevant database for our work
	def setupDB(self):
		client = MongoClient()
		return client

	@classmethod
	#Prints all items in DB, or a message if there are none
	def viewAllItems(self, database):
		cursor = database.items.find()
		
		if cursor.count() > 0:
			for document in cursor:
	    			print(document)
		else:
			print "No items in database!\n"

	@classmethod
	#Adds an item to DB
	def addItem(self, item, database):
		
		newEntry = dict(item_name=item.getName(), product_code=item.getProductCode(), price_history=item.getDatePricePair(), average_price=item.getAveragePrice())

		cursor = database.items.find({"product_code": item.getProductCode()})

		#if cursor.count > 0, item already exists
		if cursor.count() > 0:
			print "Item already defined! Enter a distinct product code or delete existing entry.\n"

		#else we can insert item
		else:
			database.items.insert(newEntry)
			print item.getName() + " inserted to database.\n"

	@classmethod
	#Adds new price contained in Item to its collected prices in DB, and also calls method to update item's average price. Updates DB with these changes.
	def updatePriceHistory(self, item, database):

		cursor = database.items.find({"product_code": item.getProductCode()})

		for document in cursor:
			#pops off price_history from mongoDB document, adds key-value pair for todays date and price, then readds price history and recalculated average price to mongoDB

			oldPriceHistory = document.pop('price_history')
			yyyymmdd = date.today().strftime("%Y%m%d")
			oldPriceHistory[yyyymmdd] = item.getDatePricePair().values().pop()

			prices = oldPriceHistory.values()

			new_average_price = MongoDBHelper.recalculateAveragePrice(prices)

			database.items.update_one({"item_name": item.getName()},
 {
        "$set": {
            "price_history": oldPriceHistory,
	    "average_price": new_average_price
        }
 }
)

		item.setAveragePrice(new_average_price)

		print item.getName() + " updated.\n"

	#Helper method to recalculate average price of an item
	@classmethod
	def recalculateAveragePrice(self, prices):

		#prices are in strings so should be converted to floats
		prices_copy = list(prices)

		prices_copy = [s.strip('$') for s in prices_copy]

		numberlist = map(float, prices_copy)

		new_average_price = (sum(numberlist)) / float(len(prices))

		return new_average_price

	@classmethod
	#Deletes a item with given product code from DB if it is present
	def deleteItem(self, product_code, database):

		result = database.items.delete_many	({"product_code": product_code})
		
		if result.deleted_count == 0:
			print "Item not found in database. Please try again.\n"
		else:
			print "Product with code " + product_code + " removed from database."
		
