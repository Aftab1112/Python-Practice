class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + " ! "

    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.__brand} - {self.__model}"

    def fuel_type(self):
        return "Petrol or diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class Electric_Car(Car):
    total_cars = 0

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        Electric_Car.total_cars += 1

    def fuel_type(self):
        return "Electric Charge"


my_tesla_car = Electric_Car("Tesla", "x", "100kWh")

print(isinstance(my_tesla_car, Car))
print(isinstance(my_tesla_car, Electric_Car))
