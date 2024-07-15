class Battery:
    def battery_info(self):
        return "I'm battery"


class Engine:
    def engine_info(self):
        return "I'm engine"


class Electric_Car(Battery, Engine):
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} - {self.model}"


my_new_tesla = Electric_Car("Tesla", "X")
print(my_new_tesla.full_name())
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
