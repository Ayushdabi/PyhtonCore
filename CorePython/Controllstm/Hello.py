'''a = 100
b = 200

if (a > b):
    print("a > b")
'''


# Class definition
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method (behavior)
    def start(self):
        print(f"{self.brand} {self.model} is starting.")


# Object creation (Instance of the class)
my_car = Car("Toyota", "Corolla")
my_car.start()