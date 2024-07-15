class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " ! "

    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.brand} - {self.model}"

    def fuel_type(self):
        return "Petrol or diesel"


class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Tata", "Harrier")
print(my_car.fuel_type())

my_electric_car = Electric_Car("Tesla", "X", 3500)
print(my_electric_car.fuel_type())
