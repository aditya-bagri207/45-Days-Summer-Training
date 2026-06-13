class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Toyota", "Fortuner", 4000000)
car2 = Car("Hyundai", "Creta", 1500000)

print(car1.brand, car1.model, car1.price)
print(car2.brand, car2.model, car2.price)