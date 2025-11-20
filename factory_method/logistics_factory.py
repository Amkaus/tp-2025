from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Vehicle):
    def deliver(self):
        return "Delivering by land in a truck"

class Ship(Vehicle):
    def deliver(self):
        return "Delivering by sea in a ship"

class Airplane(Vehicle):
    def deliver(self):
        return "Delivering by air in an airplane"

class Logistics(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

    def plan_delivery(self):
        vehicle = self.create_vehicle()
        return f"Planning delivery: {vehicle.deliver()}"

class RoadLogistics(Logistics):
    def create_vehicle(self) -> Vehicle:
        return Truck()


class SeaLogistics(Logistics):
    def create_vehicle(self) -> Vehicle:
        return Ship()

class AirLogistics(Logistics):
    def create_vehicle(self) -> Vehicle:
        return Airplane()


def test_factory_method():
    road_logistics = RoadLogistics()
    sea_logistics = SeaLogistics()
    air_logistics = AirLogistics()

    print(road_logistics.plan_delivery())
    print(sea_logistics.plan_delivery())
    print(air_logistics.plan_delivery())
    print()