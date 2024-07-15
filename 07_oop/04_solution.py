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


class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_electric_car = Electric_Car("Tesla", "X", 3500)
my_electric_car.set_brand("Nissan")
print(my_electric_car.get_brand())
