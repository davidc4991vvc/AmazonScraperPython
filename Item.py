class Item:
	name = ""
	price = 0.00
	product_code = ""
	amazon_base_url = "http://www.amazon.com/gp/product/"
	average_price = 0.00

	def __init__(self, name, price, product_code):
		self.name = name
		self.price = price
		self.product_code = product_code

	def getName(self):
		print Item.name

	def getPrice(self):
		print Item.price

	def getProductCode(self):
		print Item.product_code
	
	def getAveragePrice(self):
		print Item.average_price

	def setName(self, new_name):
		self.name = new_name
	
	def setPrice(self, new_price):
		self.price = new_price

	def setProductCode(self, new_product_code):
		self.product_code = new_product_code

	def setAveragePrice(self, new_average_price):
		self.average_price = new_average_price
