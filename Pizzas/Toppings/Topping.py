def get_price(topping_type):
    if topping_type.lower() == "cheese":
        return 20
    elif topping_type.lower() == "tomato":
        return 15
    return 0


class Topping:
    def __init__(self, type):
        self.type = type
        self.price = get_price(type)


# t = Topping("cheese")
# print(t.price)

