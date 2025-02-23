# class Car:
#     def __init__(self, brand, model):  # -----> the self is like this in javascript
#         self.brand = brand  # -----> like we used to use this.name or other thing
#         self.model = model


# # we use classes to create objects that have properties and methods
# # we can create multiple objects of the same class

# # carData = Car("BMW", "m4")
# # print(carData.brand)
# # print(carData.model)

# # methods in class


# class FullName:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def full_name(self):
#         return f"{self.firstname} {self.lastname}"  # it's in the class so we have to use self


# # nameData = FullName("Abdul", "Samad")
# # print(nameData.firstname)
# # print(nameData.lastname)
# # print(nameData.full_name())  # -----> we have to use parenthisis


# # inheritance in oop


# class Person_Detail(FullName):
#     def __init__(self, firstname, lastname, age):
#         super().__init__(firstname, lastname)
#         self.battery_capacity = age


# my_person = Person_Detail("Abdul", "Samad", "17")
# print(my_person.firstname)
# print(my_person.lastname)

# # even we can inherit methods

# print(my_person.full_name())

# in this Person_Detail class we have inherited the methods from FullName class
# and we have added a new attribute battery_capacity


# Encapsulation in oop


class AccessName:
    def __init__(self, first_name, last_name, father_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.father_name = father_name

    def get_full_Name(self):
        return f"my full name is ${self.__first_name + " " + self.__last_name} \nand my father name is {self.father_name}"


nameData = AccessName("Abdul", "Samad", "Irfan Siddique")
# print(
#     nameData.__first_name
# ) --------------> it will give error because we have used __ before the variable name which made the variable private
print(nameData.father_name)
print(nameData.get_full_Name())

# in short we use encapsulation to make variable private once we make any variable private it cant not be accessable outside the class, but we can use the private variable in the class in which the variable is declared
