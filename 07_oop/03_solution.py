class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} - {self.model}"


class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def electric_full_name(self):
        return f"{self.brand} - {self.model} - {self.battery_size}"


my_electric_car = Electric_Car("Tesla", "X", 3500)
print(my_electric_car.electric_full_name())
