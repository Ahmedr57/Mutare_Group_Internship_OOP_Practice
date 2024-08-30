# Design a system where a class Person serves as a base class with properties like name and age. 
# Create two other classes Employee and Student, which inherit from Person. 
# Then, create a class WorkingStudent that inherits from both Employee and Student. 
# Demonstrate how Python's method resolution order (MRO) works when calling methods from WorkingStudent.


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name :{self.name} , Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(self, name, age)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}$")
    

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__( name, age)
        self.grade = grade

    def display(self):
        super().display()
        print(f"Grade: {self.grade}")
        
    
class WorkingStudent(Employee, Student):
    def __init__(self, name, age, salary, grade):
        Employee.__init__(self, name, age, salary)
        Student.__init__(self, name, age, grade)

    def display(self):
        print("Working Student Information:")
        super().display()

work_std = WorkingStudent("Huzaifa", 22, 1500, "A")
work_std.display()

