from PyMongo import MongoClient

class MongoDBHelper:

	def setupDB()
		client = MongoClient()
		return client.ItemCollection

	def addItem(item, database)
		#TODO

	def updatePrice(item, newPrice, database)
		#TODO -- need to store new price in DB -- append to list
		item.setPrice(newPrice)
		
	def recalculateAveragePrice(item, prices, database)
		new_average_price = sum(prices) / float(len(prices))
		item.setAveragePrice(new_average_price)
		#TODO -- need to store new average in DB

	def deleteItem(item, database)
		#TODO
