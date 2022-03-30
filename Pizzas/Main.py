from Pizzas.Orders import Orders
from Pizzas.util import get_pizza
from Pizzas.Toppings.Topping import Topping

if __name__ == '__main__':
    order = Orders()

    print('\n1.Cheese Pizza\n2.Corn Pizza')
    num = int(input('enter type of pizza:'))

    # if num == 1:
    #     get_pizza(1)
    # if num == 2:
    #     get_pizza(2)

    pizza = get_pizza(num)

    print(' 1. Cheese 2. Tomato')
    topping_type = int(input('Enter Toppings:'))
    topping = Topping("cheese")
    if topping_type == 1:
        topping = Topping("cheese")
    elif topping_type == 2:
        topping = Topping("tomato")

    pizza.set_toppings(topping)

    print('Do you want to order pizza ?')
    order.add_order(pizza)

    print(pizza.get_prize())

    # orders = order.get_orders()
    # for o in orders:
    #     print(o.to_string())

    details = str(order.get_orders())
    print(details)
