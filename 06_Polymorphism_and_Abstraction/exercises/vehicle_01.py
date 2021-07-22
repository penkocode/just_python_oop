# 1.Vehicle
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, drive):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CAR_SUMMER_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.summer_consumption = fuel_consumption + self.CAR_SUMMER_CONSUMPTION

    def drive(self, distance):
        req_fuel = self.summer_consumption * distance
        if self.fuel_quantity >= req_fuel:
            self.fuel_quantity -= req_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    TRUCK_SUMMER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.summer_consumption = fuel_consumption + self.TRUCK_SUMMER_CONSUMPTION

    def drive(self, distance):
        req_fuel = self.summer_consumption * distance
        if self.fuel_quantity >= req_fuel:
            self.fuel_quantity -= req_fuel

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
