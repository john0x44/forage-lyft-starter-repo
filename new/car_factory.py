from datetime import date
from capulet_engine import CapuletEngine 
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine

from car import Car
from battery import NubbinBattery
from battery import SpindlerBattery

from tire import CarriganTire
from tire import OctoprimeTire

class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list):
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)