import unittest
from Item import Item

class itemTestCase(unittest.TestCase):
    def setUp(self):
	datepricepair = {'20140520': 5.79}
        self.item = Item('Sample', datepricepair, 'ABC12345')

    def tearDown(self):
        self.item.dispose()
        self.item = None

    def test_getName(self):
        self.assertEqual(self.item.getName(), 'Sample',
                         'incorrect name')

    def test_getDatePricePair(self):
        self.assertEqual(self.item.getDatePricePair(),{'20140520': 5.79}, 'incorrect date price pair')

    def test_getProductCode(self):
        self.assertEqual(self.item.getProductCode(), 'ABC12345', 'incorrect product code')

    def test_getAveragePrice(self):
        self.assertEqual(self.item.getAveragePrice(), 0.00, 'incorrect average price')

    def test_setName(self):
	self.item.setName('Name2')
        self.assertEqual(self.item.getName(), 'Name2', 'incorrect name')

    def test_setDatePricePair(self):
	self.item.setDatePricePair({'20100327': 19.16})
        self.assertEqual(self.item.getDatePricePair(),{'20100327': 19.16}, 'incorrect date price pair')

    def test_setProductCode(self):
	self.item.setProductCode('123ABQ')
        self.assertEqual(self.item.getProductCode(), '123ABQ', 'incorrect product code')

    def test_setAveragePrice(self):
	self.item.setAveragePrice(4.37)
	self.assertEqual(self.item.getAveragePrice(), 4.37, 'incorrect average price')

    def suite():
	tests = ['test_getName', 'test_getDatePricePair', 'test_getProductCode', 'test_getAveragePrice', 'test_setName', 'test_setDatePricePair', 'test_setProductCode', 'test_setAveragePrice']

	return unittest.TestSuite(map(itemTestCase, tests))
