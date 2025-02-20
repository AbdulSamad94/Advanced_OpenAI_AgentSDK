class Car:
    def __init__(self, brand, model):  # -----> the self is like this in javascript
        self.brand = brand  # -----> like we used to use this.name or other thing
        self.model = model


# we use classes to create objects that have properties and methods
# we can create multiple objects of the same class

# carData = Car("BMW", "m4")
# print(carData.brand)
# print(carData.model)

# methods in class


class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"  # it's in the class so we have to use self


# nameData = FullName("Abdul", "Samad")
# print(nameData.firstname)
# print(nameData.lastname)
# print(nameData.full_name())  # -----> we have to use parenthisis


# inheritance in oop


class Person_Detail(FullName):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname)
        self.battery_capacity = age


my_person = Person_Detail("Abdul", "Samad", "17")
print(my_person.firstname)
print(my_person.lastname)

# even we can inherit methods

print(my_person.full_name())
