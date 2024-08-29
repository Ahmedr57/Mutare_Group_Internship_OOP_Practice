# 1.	Create a class Student that has properties for the student's name, age, and grades (as a list). Implement methods to add a grade, 
# calculate the average grade, and display the student's information in a formatted string. Instantiate multiple Student 
# objects and demonstrate their use.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age 
        self.grades = grades

    def add_grades(self, grade):
        self.grades.append(grade)

    def get_average_grades(self):
        if len(self.grades) == 0:
            return 0
        else : 
            return sum(self.grades)/len(self.grades)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grades: {self.get_average_grades():.2f}")




std1 = Student("Ali", 20, [98, 88, 75] )
std1.display_info()
std1.add_grades(58)
std1.display_info()


std2 = Student("Shahid", 21, [72, 86, 93] )
std2.add_grades(99)
std2.add_grades(81)
std2.display_info()