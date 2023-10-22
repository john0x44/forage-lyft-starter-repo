from datetime import date
from engine import Engine

class SternmanEngine(Engine):
    def __init__(self, last_service_date: date, warning_light_on: bool):
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on