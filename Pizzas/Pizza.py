class Pizza:
    def get_contents(self):
        pass

    def get_toppings(self):
        pass

    def get_base(self):
        pass

    def set_toppings(self, topping):
        pass

    def set_base_soft(self):
        pass

    def set_base_hard(self):
        pass

    def get_prize(self):
        price = 0
        price = price + (len(self.get_contents()) * 10)
        if self.get_base().lower() == "hard".lower():
            price = price + 20
        for topping in self.get_toppings():
            price = price + topping.price
        return price

    def to_string(self):
        pass