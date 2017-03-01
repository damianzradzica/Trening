next_id = 0
class Product(object):
    def __init__(self, name, description, price, quantity):
        global next_id
        self.id = next_id
        next_id += 1
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Nieprawidłowa wartość name')
        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError('Nieprawidłowa wartość description')
        if isinstance(price, float):
            self.price = price
        else:
            raise ValueError('Nieprawidłowa wartość price')
        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            raise ValueError('Nieprawidłowa wartość quantity')

    def get_total_sum(self):
        result = self.quantity * self.price
        return result

class ShoppingCart(object):
    def __init__(self):
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def remove_product(self, product_id):
        for prod in self.products:
            if prod.id == product_id:
                self.products.remove(prod)

    def change_product_quantity(self, product_id, new_quantity):
        for prod in self.products:
            if prod.id == product_id:
                self.products.quantity = new_quantity




