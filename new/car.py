from abc import ABC
from engine import Engine 
from battery import Battery 

# car.py
from abc import ABC

class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery, tire_wear: list):
        self.engine = engine
        self.battery = battery
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return (
            self.engine.needs_service() or
            self.battery.needs_service() or
            self.tire_needs_service()
        )

    def tire_needs_service(self) -> bool:
        return False
    
