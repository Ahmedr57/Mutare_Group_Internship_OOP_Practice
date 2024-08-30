# Create a base class Employee with properties like name and salary, and a method calculate_bonus(). 
# Derive two classes Manager and Developer that override the calculate_bonus() method to provide different bonus calculations based on their roles.
# Write a function that accepts a list of Employee objects and uses polymorphism to calculate the total bonuses for all employees dynamically.

class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculate_bonus(self):
        print(f"Salary of {self.name} before adding Bonus: {self.salary}$")
        self.salary += self.salary * 0.15
        print(f"Salary of {self.name} after adding Bonus: {self.salary}$")
        
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculate_bonus(self):
        print(f"Salary of {self.name} before adding Bonus: {self.salary}$")
        self.salary += self.salary * 0.25
        print(f"Salary of {self.name} after adding Bonus: {self.salary}$")


per1 = Manager("John", 5000)
per2 = Manager("Jack", 4000)
per3 = Developer("Jordan", 6500)
per4 = Developer("Julie", 3500)


list_per =[ per1, per2, per3, per4 ]

def bonus_cal(lis):
    for item in lis:
        item.calculate_bonus()

bonus_cal(list_per)