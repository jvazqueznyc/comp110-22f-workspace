"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza in order to calculate its price."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool


    def price(self, tax: float) -> float:  # Method call. Our pizzas calculate their own price.
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total += tax

        return total
    
    # def price(pizza: Pizza) -> float:  # parameter is named pizza and it is an object of class Pizza.
#     total: float = 0.0
#     if pizza.size == "large":
#         total += 10.0
#     else:
#         total += 8.0

#     total += pizza.toppings * 0.75

#     if pizza.extra_cheese:
#         total += 1.0

#     return total


a_pizza: Pizza =  Pizza()  # Pizza() is a constructor call. a_pizza variable is type pizza and maps to the new pizza object 'pizza'.
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")