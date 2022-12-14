class PizzaBase(type):
   _instances = {}
   def __call__(cls, *args, **kwargs):
       if cls not in cls._instances:
           cls._instances[cls] = super(PizzaBase, cls).\
               __call__(*args, **kwargs)
       return cls._instances[cls]

class PizzaType(metaclass=PizzaBase):
    def __init__(self):
        self.name = "Margarita"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


if __name__ == "__main__":
    Margarita = PizzaType()
    Chicken = PizzaType()
    print("Pizza1 name: " + Margarita.get_name())
    Margarita.set_name("Chicken")
    print("Pizza2 name: " + Chicken.get_name())
    print(Margarita)
    print(Chicken)
    print(id(Margarita) == id(Chicken))