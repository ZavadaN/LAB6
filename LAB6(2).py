from enum import Enum

class PizzaType(Enum):

    MARGARITA = 0,
    CHIKEN = 1,


class Pizza:
   
    def __init__(self, price: float):
        self.__price = price # цена пиццы
    def get_price(self) -> float:
        return  self.__price

class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(560)


class PizzaChiken(Pizza):
    def __init__(self):
        super().__init__(689)


def create_pizza(pizza_type: PizzaType) -> Pizza:
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.CHIKEN: PizzaChiken
    }
    return factory_dict[pizza_type]()

if __name__ == '__main__':
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f' Pizza type: {pizza}, price: {my_pizza.get_price()}')