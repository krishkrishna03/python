# Day 18: Object-Oriented Programming (OOP) Example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

# Create an object
my_car = Car("Toyota", "Innova")
my_car.start()
