import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("Ab")
        with self.assertRaises(ValueError):
            Coffee(123)

    def test_orders_and_customers(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertIn(order, self.coffee.orders())
        self.assertIn(self.customer, self.coffee.customers())

    def test_num_orders_and_average_price(self):
        Order(self.customer, self.coffee, 5.0)
        Order(self.customer, self.coffee, 7.0)
        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertEqual(self.coffee.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()