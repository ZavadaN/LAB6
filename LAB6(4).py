from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class OrderType(Enum):
    MARGARITA = 1
    CHICKEN = 2


class Order:
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"заказ под #{self.id} ({self.type.name})"


class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...


class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)


class Povar(Subject):
   def __init__(self):
       super().__init__()
       self.__orders: List[Order] = []
       self.__finish_order: List[Order] = []
   def take_order(self, order: Order) -> None:
       print(f"Шеф-повар принял  {order}")
       self.__orders.append(order)
   def get_order(self, order_id: int) -> Order:
       order = None
       for it in self.__finish_order:
           if it.id == order_id:
              order = it
              break
       self.__finish_order.remove(order)
       return order

   def processing_order(self):
       if self.__orders:
           order = choice(self.__orders)
           self.__orders.remove(order)
           self.__finish_order.append(order)
           print(f"Заказ готов, пицца -  {order}")
           self.notify(order.id)
       else:
           print("Шеф-повар готовит основы для пиццы")


class Client(Observer):
    def __init__(self, name: str, barista: Povar):
        self.__barista = barista
        self.__name = name
        self.order: Order = None

    def update(self, order_id: int) -> None:
        if self.order is not None:
           if order_id == self.order.id:
              print(f"Клиент {self.__name} получил "
                    f"{self.__barista.get_order(order_id)}")
              self.__barista.detach(self)

    def create_order(self) -> None:
        order_type = choice([OrderType.MARGARITA,
                             OrderType.CHICKEN])
        self.order = Order(order_type)
        print(f"Клиент {self.__name} выбрал {self.order}")
        self.__barista.attach(self)
        self.__barista.take_order(self.order)


if __name__ == "__main__":
     names = ['Кристина', 'Анастасия',
              'Виктор']
     Shef = Povar()
     clients = [Client(name, Shef) for name in names]
     for client in clients:
         print("*"*30)
         client.create_order()
     print("*" * 4 + "Шеф-повар приступает к выполнению заказов" + 4 * "*")
     for _ in range(6):
         print("*" * 30)
         Shef.processing_order()

