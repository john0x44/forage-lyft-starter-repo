# Testing goes in here 

from datetime import date

from car_factory import CarFactory

# Create a CarFactory instance
factory = CarFactory()

# Test 1 : Create a Calliope car
current_date = date(2024, 10, 22)
last_service_date = date(2020, 10, 22)
current_mileage = 40000
last_service_mileage = 30000

car = factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)

needs_service = car.needs_service()

if needs_service:
    print("The car needs service.")
else:
    print("The car does not need service.")
