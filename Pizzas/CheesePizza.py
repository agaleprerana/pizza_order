from Pizzas.Pizza import Pizza


class CheesePizza(Pizza):
    def __init__(self):
        self.topping = []
        self.base = "soft"

    def get_contents(self):
        return ["Cheese"]

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

    def to_string(self):
        ret = "Cheese Pizza" + self.get_base() + " ";
        join = ret.join(x for x in self.get_toppings())
        for topping in self.get_toppings():
            ret = ret + topping.type + " "
        return ret
