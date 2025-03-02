class Employee:
    name = "Abdul Samad"
    salary = "1200000"

    @staticmethod  # -------------------> we use this because we don't need to create an object of the class to access the static method
    def name_and_salary():
        print(f"your salary is good")


employee_data = Employee()

employee_data.name_and_salary()  # -----> and we try to run it without @staticmethod it will give an error because we are trying to access the static method without creating an object of the class
