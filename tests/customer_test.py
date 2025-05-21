import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)
        with self.assertRaises(ValueError):
            Customer(123)

    def test_name_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        with self.assertRaises(ValueError):
            self.customer.name = "A" * 16

    def test_orders_and_coffees(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertIn(order, self.customer.orders())
        self.assertIn(self.coffee, self.customer.coffees())

if __name__ == "__main__":
    unittest.main()