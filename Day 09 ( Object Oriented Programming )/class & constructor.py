class Cars:
    name = "BMW"
    model = "m3"


get_car = Cars()
print(get_car.name, get_car.model)


# constructor


class Car:
    def __init__(self, brand, model):  # -----> the self is like this in javascript
        self.brand = brand  # -----> like we used to use this.name or other thing
        self.model = model


# we use classes to create objects that have properties and methods
# we can create multiple objects of the same class

carData = Car("BMW", "m4")
print(carData.brand)
print(carData.model)
