class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def total_price(self):
        return sum(product.price for product in self.items)

    def list_products(self):
        print("Shopping Cart Items:")
        for product in self.items:
            print(f"- {product.name}: ${product.price}")

# Usage
cart = ShoppingCart()
p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 25)

cart.add_product(p1)
cart.add_product(p2)
cart.list_products()
print(f"Total: ${cart.total_price()}")
