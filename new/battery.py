from datetime import date
from servicable import Serviceable

class Battery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date.year - self.last_service_date.year) >= 2

class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date.year - self.last_service_date.year) >= 3

class NubbinBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date.year - self.last_service_date.year) >= 2