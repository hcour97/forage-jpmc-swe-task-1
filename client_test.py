import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (bid_price + ask_price) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    bid_price_ABC = quotes[0]['top_bid']['price']
    ask_price_ABC = quotes[0]['top_ask']['price']

    bid_price_DEF = quotes[1]['top_bid']['price']
    ask_price_DEF = quotes[1]['top_ask']['price']
     
    self.assertGreater(bid_price_ABC, ask_price_ABC, "ABC bid price > ABC ask price")
    self.assertGreater(ask_price_DEF, bid_price_DEF, "DEF ask price > DEF bid price")

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_normal(self):
    self.assertEqual(getRatio(2,1), 2.000)
    self.assertEqual(getRatio(1000, 500), 2)
  
  def test_getRatio_divideByZero(self):
    self.assertEqual(getRatio(2, 0), None)
    self.assertEqual(getRatio(-5000, 0), None)

  def test_getRatio_numeratorZero(self):
    self.assertEqual(getRatio(0, 80), 0.00000)

  def test_getRatio_Negative(self):
    self.assertEqual(getRatio(-2, -1), 2)
    self.assertEqual(getRatio(-5000, 500), -10)
    self.assertEqual(getRatio(20, -5), -4)

if __name__ == '__main__':
    unittest.main()
