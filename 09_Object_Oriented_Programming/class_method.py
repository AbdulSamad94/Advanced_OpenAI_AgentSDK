# class Random_Number:
#     number = 3

#     def get_Number(self):
#         print(f"Your Number is {self.number}")


# Data = Random_Number()
# Data.number = 45

# Data.get_Number() it will print 45 because we have changed its value below

# we use class method to access the number that is in the class only even if we change its value below it will always print the attribute that we gave in the class


class Random_Number:
    number = 3

    @classmethod
    def get_Number(self):
        print(f"Your Number is {self.number}")


Data = Random_Number()
Data.number = 45

Data.get_Number()  # in this it will give the number 3 even if we have changed its value
