# inheritance in oop
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
