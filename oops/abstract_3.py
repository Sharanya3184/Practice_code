from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike started")

class Car(Vehicle):
    def start(self):
        print("Car started")


b = Bike()
c = Car()
c.start()  
