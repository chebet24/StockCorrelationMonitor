import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
class TestGetRatio(unittest.TestCase):
    
    def test_positive_numbers(self):
        """Test with two positive numbers"""
        self.assertEqual(getRatio(10, 2), 5)
        self.assertEqual(getRatio(9, 3), 3)

    def test_zero_numerator(self):
        """Test when the numerator is zero"""
        self.assertEqual(getRatio(0, 5), 0)

    def test_zero_denominator(self):
        """Test when the denominator is zero"""
        self.assertIsNone(getRatio(10, 0))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(getRatio(-10, -2), 5)
        self.assertEqual(getRatio(-9, 3), -3)

    def test_fractional_numbers(self):
        """Test with fractional numbers"""
        self.assertAlmostEqual(getRatio(1.5, 0.5), 3.0)
        self.assertAlmostEqual(getRatio(7.5, 2.5), 3.0)




if __name__ == '__main__':
    unittest.main()
