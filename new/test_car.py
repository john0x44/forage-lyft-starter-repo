import unittest
from datetime import date
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from battery import SpindlerBattery
from battery import NubbinBattery
from tire import CarriganTire, OctoprimeTire

# Create a test class for Engine, Battery, and Tire
class EngineBatteryTireTest(unittest.TestCase):
    
    def test_capulet_engine(self):
        last_service_date = date(2021, 10, 22)
        current_mileage = 40000
        last_service_mileage = 30000

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine(self):
        last_service_date = date(2021, 10, 22)
        warning_light_on = True

        engine = SternmanEngine(last_service_date, warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine(self):
        last_service_date = date(2021, 10, 22)
        current_mileage = 80000
        last_service_mileage = 70000

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_spindler_battery(self):
        last_service_date = date(2021, 10, 22)
        current_date = date(2023, 10, 22)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery(self):
        last_service_date = date(2022, 10, 22)
        current_date = date(2021, 10, 22)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_carrigan_tire_needs_service(self):
        tire_wear = [0.9, 0.85, 0.88]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.tire_needs_service())

    def test_carrigan_tire_does_not_need_service(self):
        tire_wear = [0.7, 0.8, 0.75]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.tire_needs_service())

    def test_octoprime_tire_needs_service(self):
        tire_wear = [1.0, 0.8, 1.2]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.tire_needs_service())

    def test_octoprime_tire_does_not_need_service(self):
        tire_wear = [0, 0, 0, 0]
        tire = OctoprimeTire(tire_wear)
        print("OCTOPRIME TIRES NEED SERVICE?:  " + str(tire.tire_needs_service()))
        self.assertFalse(tire.tire_needs_service())

if __name__ == '__main__':
    unittest.main()
