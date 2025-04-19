from dataclasses import dataclass, field

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name={self.name}, age={self.age})"

#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age


# output = Person("John Doe", 30)
# print(output.name, output.age)

# The same thing can be done with dataclasses, which will make this work much easier to read and maintain.


@dataclass
class Person:
    name: str
    age: int

    


output = Person("John Doe", 30)
print(output.name, output.age)
