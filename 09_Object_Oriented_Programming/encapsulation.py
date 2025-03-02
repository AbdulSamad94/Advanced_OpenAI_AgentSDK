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
