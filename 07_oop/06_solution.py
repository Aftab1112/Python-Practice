class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + " ! "

    def set_brand(self, brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.brand} - {self.model}"

    def fuel_type(self):
        return "Petrol or diesel"


class Electric_Car(Car):
    total_cars = 0

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        Electric_Car.total_cars += 1

    def fuel_type(self):
        return "Electric Charge"


Car("Tata", "Harrier")
Car("Toyota", "Fortuner")
Car("BMW", "I4")

print(Car.total_cars)
print(Electric_Car.total_cars)
