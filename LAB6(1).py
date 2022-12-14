from abc import ABC, abstractmethod

class IPizzaBase(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass


class PizzaBase(IPizzaBase):
   def __init__(self, cost):
       self.__cost = cost

   def cost(self) -> float:
       return self.__cost


class IDecorator(IPizzaBase):
    @abstractmethod
    def name(self) -> str:
        pass


class PizzaMargarita(IDecorator):

    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
         self.__wrapped = wrapped
         self.__cost = pizza_cost
         self.__name = "Маргарита"

    def cost(self) -> float:
         return self.__cost+self.__wrapped.cost()

    def name(self) -> str:
         return self.__name

class PizzaChiken(IDecorator):

    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Куриная"

    def cost(self) -> float:
            return (self.__cost + self.__wrapped.cost()) * 1.25

    def name(self) -> str:
            return self.__name

if __name__ == "__main__":
     def print_pizza(pizza: IDecorator) -> None:
         print(f"Стоимость пиццы '{pizza.name()}' = {pizza.cost()} ")

     pizza_base = PizzaBase(300)
     print(f"Стоимость основы пиццы = {pizza_base.cost()}")
     margarita = PizzaMargarita(pizza_base, 100)
     print_pizza(margarita)
     chiken = PizzaChiken(pizza_base, 200)
     print_pizza(chiken)
