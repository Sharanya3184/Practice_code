from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        return "Petrol or Diesel"

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"


my_car = Car()
print(my_car.start_engine())  
