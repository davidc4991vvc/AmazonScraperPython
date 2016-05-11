class Item:
	name = ""
	date_price_pair = ""
	product_code = ""
	amazon_base_url = "http://www.amazon.com/gp/product/"
	average_price = 0.00

	def __init__(self, name, date_price_pair, product_code):
		self.name = name
		self.date_price_pair = date_price_pair
		self.product_code = product_code

	def getName(self):
		return self.name

	def getDatePricePair(self):
		return self.date_price_pair

	def getProductCode(self):
		return self.product_code
	
	def getAveragePrice(self):
		return self.average_price

	def setName(self, new_name):
		self.name = new_name
	
	def setDatePricePair(self, new_date_price_pair):
		self.date_price_pair = new_date_price_pair

	def setProductCode(self, new_product_code):
		self.product_code = new_product_code

	def setAveragePrice(self, new_average_price):
		self.average_price = new_average_price
