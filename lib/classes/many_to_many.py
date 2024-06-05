# Import the mean function from the statistics module
from statistics import mean

# Define the Customer class
class Customer:
    # List to store all Customer instances
    all = []

    # Initialize a new Customer instance
    def __init__(self, username):
        self.name = username
        self.all.append(self)

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def name(self):
        return self._name

    # Setter for name property
    @name.setter
    def name(self, username):
        # Check if the name is a string and its length is between 1 and 15 characters
        if isinstance(username, str) and 1 <= len(username) <= 15:
            self._name = username
        else:
            raise Exception("Invalid name")

    # Method to get the orders of the customer
    def orders(self):
        # Return a list of orders where the customer is the current customer
        return [order for order in Order.all if order.customer is self]

    # Method to get the coffees ordered by the customer
    def coffees(self):
        # Return a list of unique coffees that the customer has ordered
        return list({order.coffee for order in self.orders()})

    # Method to create a new order for the customer
    def create_order(self, new_coffee, new_price):
        return Order(self, new_coffee, new_price)

    # Class method to get the customer who has ordered the most of a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
        if coffee_all_orders := [
            order for order in Order.all if order.coffee is coffee
        ]:
            return max(
                cls.all,
                key=lambda customer: sum(
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        return None


# Define the Coffee class
class Coffee:
    # Initialize a new Coffee instance
    def __init__(self, title):
        self.name = title

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, title):
        if hasattr(self, "_name"):
            raise Exception ("Name is immutable")
        if isinstance(title, str) and len(title) >=3:
            self._name = title
        else:
            raise Exception ("Invalid name")




    # Method to get the orders of the coffee
    def orders(self):
        # Return a list of orders where the coffee is the current coffee
        return [order for order in Order.all if order.coffee is self]

    # Method to get the customers who have ordered the coffee
    def customers(self):
        # Return a list of unique customers who have ordered the current coffee
        return list({order.customer for order in self.orders()})

    # Method to get the number of orders of the coffee
    def num_orders(self):
        return len(self.orders())

    # Method to get the average price of the coffee
    def average_price(self):
        return mean([order.price for order in self.orders()])


# Define the Order class
class Order:
    # List to store all Order instances
    all = []

    # Initialize a new Order instance
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price  # Initialize _price attribute
        self.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, "_price"):
            raise Exception("Price is immutable")
        if isinstance(price, float) and 1.0 <= price <= 10.0: 
            self._price = price
        else:
            raise Exception("Invalid price")

    

    # Property decorator allows us to define a method but access it like an attribute
    @property
    def coffee(self):
        return self._coffee

    # Setter for coffee property
    @coffee.setter
    def coffee(self, coffee):
        # Check if the coffee is an instance of the Coffee class
        if isinstance(coffee, Coffee):
            self._coffee = coffee
