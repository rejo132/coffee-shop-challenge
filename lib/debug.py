from customer import Customer
from coffee import Coffee
from order import Order

# Example usage
if __name__ == "__main__":
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    order1 = customer1.create_order(coffee1, 5.0)
    order2 = customer1.create_order(coffee2, 3.0)
    order3 = customer2.create_order(coffee1, 6.0)

    print(f"{customer1.name}'s orders: {len(customer1.orders())}")
    print(f"{coffee1.name}'s average price: {coffee1.average_price()}")
    print(f"Most aficionado for {coffee1.name}: {Customer.most_aficionado(coffee1).name}")