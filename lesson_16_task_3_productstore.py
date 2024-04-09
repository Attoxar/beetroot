class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.type}) - Price: ${self.price:.2f}"


class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        if product.name not in self.products:
            self.products[product.name] = {'product': product, 'amount': amount}
        else:
            self.products[product.name]['amount'] += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product_info in self.products.values():
            if identifier_type == 'name' and product_info['product'].name == identifier:
                product_info['product'].price *= (1 - percent / 100)
            elif identifier_type == 'type' and product_info['product'].type == identifier:
                product_info['product'].price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name not in self.products or self.products[product_name]['amount'] < amount:
            raise ValueError(f"Not enough {product_name} in the store.")
        else:
            self.products[product_name]['amount'] -= amount

    def get_income(self):
        return sum(product_info['product'].price * product_info['amount'] for product_info in self.products.values())

    def get_all_products(self):
        return self.products.values()

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"{product_name} is not available in the store.")
        else:
            product_info = self.products[product_name]
            return product_info['product'].name, product_info['amount']

    def print_available_products(self):
        print("Available products in the store:")
        for product_info in self.products.values():
            print(product_info['product'])
            print(f"Amount available: {product_info['amount']}")
            print()


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

s.print_available_products()
