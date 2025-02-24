class FullName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"  # it's in the class so we have to use self


nameData = FullName("Abdul", "Samad")
print(nameData.firstname)
print(nameData.lastname)
print(nameData.full_name())  # -----> we have to use parenthisis
