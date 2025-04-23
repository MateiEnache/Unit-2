class Pizza:
    total_cost = 0

    def __init__(self, size, topping, price, flavor):
        self.size = size
        self.topping = topping
        self.price = price
        self.flavor = flavor
        Pizza.total_cost += price

    def __repr__(self):
        return f"The {self.size} inch pizza with {self.topping} and {self.flavor} costs ${self.price:.2f}."

    def __eq__(self, other):
        if self.flavor == other.flavor and self.price == other.price and self.size == other.size and self.topping == other.topping:
            return True
        return False

    def __add__(self, other):
        return self.price + other.price

class Deep_Dish(Pizza):
    def __init__(self, size, topping, price, flavor):
        super().__init__(size, topping, price, flavor)
        self.price *= 1.2

    def __repr__(self):
        return f"The {self.size} inch deep dish pizza with {self.topping} and {self.flavor} costs ${self.price:.2f}."

    def deep_dish_extras(self):
        return f"This pizza has 25% more {self.topping} because it's a deep dish!"

class Thin_Crust(Pizza):
    def __init__(self, size, topping, price, flavor):
        super().__init__(size, topping, price, flavor)
        self.price *= 0.9  # Thin crust is 10% cheaper

    def __repr__(self):
        return f"The {self.size} inch thin crust pizza with {self.topping} and {self.flavor} costs ${self.price:.2f}."

    def thin_crust_extras(self):
        return f"This pizza has a crispy, thin crust for a light and crispy bite!"

piza1 = Pizza(11, "cheese", 15, "tomato")
deep_dish_pizza = Deep_Dish(12, "sausage", 20, "garlic")
thin_crust_pizza = Thin_Crust(10, "pepperoni", 18, "spicy")

print(piza1)
print(deep_dish_pizza)
print(deep_dish_pizza.deep_dish_extras())
print(thin_crust_pizza)
print(thin_crust_pizza.thin_crust_extras())
print("Total cost of all pizzas so far:", f"${Pizza.total_cost:.2f}")
print(piza1 == thin_crust_pizza)
