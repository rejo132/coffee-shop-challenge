import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")

    def test_properties(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

if __name__ == "__main__":
    unittest.main()