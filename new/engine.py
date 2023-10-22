from abc import ABC
from servicable import Serviceable
from datetime import date 

class Engine(Serviceable, ABC):
    pass

class CapuletEngine(Engine):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) >= 30000