from pymongo import MongoClient
from Item import Item
from datetime import date

class MongoDBHelper:
	
	@classmethod
	#Setup DB client and returns relevant database for our work
	def setupDB(self):
		client = MongoClient()
		return client.ItemCollection

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

		newEntry = dict(name=item.getName(), product_code=item.getProductCode(), price_history=item.getDatePricePair(), average_price=item.getAveragePrice())

		database.items.insert_one(newEntry)
		print newEntry + " inserted to database.\n"

	@classmethod
	#Adds new price contained in Item to its collected prices in DB, and also calls method to update item's average price. Updates DB with these changes.
	def updatePriceHistory(self, item, database):

		cursor = database.items.find({"product_code": item.getProductCode()})

		for document in cursor:
			oldPriceHistory = document.pop(price_history)
			oldPriceHistory[date.today()] = item.getDatePricePair().values().pop()

			document[price_history] = oldPriceHistory

			prices = oldPriceHistory.values()
			new_average_price = recalculateAveragePrice(prices)

			database.items.update_one({"name": item.getName()},
 {
        "$set": {
            "price_history": oldPriceHistory,
	    "average_price": new_average_price
        }
 }
)

		print item.getName() + " updated.\n"

	#Helper method to recalculate average price of an item
	def recalculateAveragePrice(prices):
		new_average_price = sum(prices) / float(len(prices))
		item.setAveragePrice(new_average_price)

		return new_average_price

	@classmethod
	#Deletes a item with given product code from DB if it is present
	def deleteItem(self, product_code, database):

		result = database.items.delete_many	({"product_code": product_code})
		
		if result.deleted_count == 0:
			print "Item not found in database. Please try again.\n"
		else:
			print result + " removed from database."
		
