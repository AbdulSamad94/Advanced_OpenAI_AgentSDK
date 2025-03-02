# inheritance in oop


class Car_one:
    name = "BMW"
    model = "m3"


class Car_two(Car_one):
    name_two = "Mercedes-Benz"
    model_two = "G"


class Car_three(Car_two):
    name_three = "Audi"
    model_three = "A4"


# cars = Car_one()
# print(cars.name, cars.model, cars.name_two)  ------> it will give error as they are not in the same class

# we can inherit multiple classes

cars = Car_three()
print(
    cars.name_three, cars.model
)  # -------> in this we are getting multiple classes atribute from the class we inherited


# super in inheritance

# we use super to access the __init__ method of the parent class


class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"


class Person_Detail(FullName):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname)
        self.battery_capacity = age


my_person = Person_Detail("Abdul", "Samad", "17")
print(my_person.firstname)
print(my_person.lastname)

# even we can inherit methods

print(my_person.full_name())

# in this Person_Detail class we have inherited the methods from FullName class
# and we have added a new attribute battery_capacity
