from statistics import mean


class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return mean([order.price for order in self.orders()])


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        most = None
        most_spent = 0
        for customer in cls.all:
            cust_total = sum([order.price for order in self.orders(customer)])
            if cust_total > most_spent:
                most_spent = cust_total
                most = customer
        return most


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            not hasattr(self, "price")
            and isinstance(price, float)
            and 1.0 <= price <= 10.0
        ):
            self._price = price
