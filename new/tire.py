from abc import ABC

class Tire(ABC):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def tire_needs_service(self) -> bool:
        return False 

class CarriganTire(Tire):
    def tire_needs_service(self) -> bool:
        return any(wear >= 0.9 for wear in self.tire_wear)

class OctoprimeTire(Tire):
    def tire_needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3