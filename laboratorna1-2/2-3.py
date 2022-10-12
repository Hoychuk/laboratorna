class Product:
    def __init__(self, price, description):
        if price < 0:
            raise ValueError
        if not isinstance(price, int):
            raise TypeError("Wrong data")
        self.price = price
        self.description = description

    def __str__(self):
        return f'Price of {self.description} is {self.price}'


class Customer:
    def __init__(self, surname, name, mobile_phone):
        if not isinstance(mobile_phone, (int, float)):
            raise TypeError("Wrong data")
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'Customer is {self.surname} {self.name}, phone number: {self.mobile_phone}'


class Order:
    def __init__(self, customer, *product):
        if not isinstance(customer, Customer):
            raise TypeError("Wrong data customer")
        for i in product:
            if not isinstance(i, Product):
                raise TypeError("Wrong data products")
        self.customer = customer
        self.products = []
        self.products_number = []
        for i in product:
            self.Add_Product(i)
        self.cost = 0

    def Add_Product(self, product):
        if product in self.products:
            self.products_number[self.products.index(product)] += 1
        else:
            self.products.append(product)
            self.products_number.append(1)

    def Delete_Product(self, product):
        if product in self.products:
            if self.products_number[self.products.index(product)] > 1:
                self.products_number[self.products.index(product)] -= 1
            else:
                self.products.pop(self.products.index(product))
                self.products_number.pop(self.products.index(product))

    def __Calculate_Order(self):
        self.cost = 0
        for i in self.products:
            self.cost += i.price * self.products_number[self.products.index(i)]
        return self.cost

    def __str__(self):
        return f'Price of order of {self.customer.surname} {self.customer.name} is {self.__Calculate_Order()}'


test = Customer("Sasha", "Hoychuk", 380666889700)
product1 = Product(10, "Rubik`s cube")
product2 = Product(5, "Pan")
product3 = Product(2, "Apple")
order = Order(test, product1, product2, product3)
order.Add_Product(product1)
order.Add_Product(product2)
order.Add_Product(product3)
order.Delete_Product(product2)
print(order)