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
        self.customer2 = Customer("Bob")
        self.coffee = Coffee("Latte")

    def tearDown(self):
        Customer._all.clear()
        Coffee._all.clear()
        Order._all.clear()

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

    def test_most_aficionado(self):
        # Alice orders Latte for $5.0 and $3.0 (total $8.0)
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 3.0)
        # Bob orders Latte for $4.0
        self.customer2.create_order(self.coffee, 4.0)
        # Alice should be the most aficionado
        self.assertEqual(Customer.most_aficionado(self.coffee), self.customer)
        # Test no orders
        new_coffee = Coffee("Espresso")
        self.assertIsNone(Customer.most_aficionado(new_coffee))

if __name__ == "__main__":
    unittest.main()