from Pizzas.Pizza import Pizza


class Corn_Pizza(Pizza):
    def __init__(self):
        self.topping = []
        self.base = "soft"

    def get_contents(self):
        return ["Corn"]

    def get_toppings(self):
        return self.topping

    def get_base(self):
        return self.base

    def set_base_soft(self):
        self.base = "soft"

    def set_base_hard(self):
        self.base = "hard"

    def set_toppings(self, topping):
        self.topping.append(topping)

