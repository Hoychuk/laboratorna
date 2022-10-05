class Product:
    def __init__(self, price, description):
        if price < 0:
            raise ValueError
        self.price = price
        self.description = description


class Customer:
    def __init__(self, surname, name, mobile_phone):
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone


class Order:
    def __init__(self, customer, *product):
        self.customer = customer
        self.products = product
        self.cost = 0

    def __Calculate_Order(self):
        self.cost = 0
        for i in self.products:
            self.cost += i.price
        return self.cost

    def __str__(self):
        return f'Price of order of {self.customer.surname} {self.customer.name} is {self.__Calculate_Order()}'


test = Customer("Sasha", "Hoychuk", 380666889700)
product1 = Product(10, "Rubik`s cube")
product2 = Product(5, "Pan")
product3 = Product(2, "Apple")
order = Order(test, product1, product2, product3)
print(order)