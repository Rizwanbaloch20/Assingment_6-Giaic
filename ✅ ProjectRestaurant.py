class FoodItem:
    def get_description(self):
        return "Unknown Food Item"

    def get_cost(self):
        return 0

class Pizza(FoodItem):
    def get_description(self):
        return "Pizza"

    def get_cost(self):
        return 10

class FoodDecorator(FoodItem):
    def __init__(self, food_item):
        self.food_item = food_item

class Cheese(FoodDecorator):
    def get_description(self):
        return self.food_item.get_description() + ", Cheese"

    def get_cost(self):
        return self.food_item.get_cost() + 2

class Olives(FoodDecorator):
    def get_description(self):
        return self.food_item.get_description() + ", Olives"

    def get_cost(self):
        return self.food_item.get_cost() + 1.5

# Usage
order = Pizza()
order = Cheese(order)
order = Olives(order)

print(f"Order: {order.get_description()}")
print(f"Total Cost: ${order.get_cost()}")
