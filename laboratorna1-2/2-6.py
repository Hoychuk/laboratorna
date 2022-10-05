import random


class Binary:
    def __init__(self, product_code, price):
        self.product_code = product_code
        self.price = price
        self.leaf_left = None
        self.leaf_right = None

    def add_element(self, leaf):
        if leaf.product_code <= self.product_code:
            if self.leaf_left:
                self.leaf_left.add_element(leaf)
            else:
                self.leaf_left = leaf
        if leaf.product_code > self.product_code:
            if self.leaf_right:
                self.leaf_right.add_element(leaf)
            else:
                self.leaf_right = leaf

    def find_product(self, product_code, quantity):
        if self.product_code == product_code:
            return quantity * self.price
        if self.leaf_left:
            if self.product_code > product_code:
                return self.leaf_left.find_product(product_code, quantity)
        if self.leaf_right:
            if self.product_code < product_code:
                return self.leaf_right.find_product(product_code, quantity)
        raise ValueError("Not founded an product code")


random.seed()
tree = Binary(1, 50)
for i in range(2, 100):
    tree.add_element(Binary(i, random.randrange(1, 100)))
print(tree.find_product(5, 100))