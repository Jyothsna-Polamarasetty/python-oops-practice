# Coding Exercise 1
# Create:
# class Student
# Attributes:
# Name
# Age
# Marks
# Methods:
# display()
# calculate_grade()
# Grades:
# 90-100 → A
# 80-89 → B
# 70-79 → C
# 60-69 → D
# Below 60 → F

class Student:
    def __init__(self,Name, Age, Marks):
        self.Name = Name
        self.Age = Age
        self.Marks = Marks
    def display(self):
        print(f"Name : {self.Name}")
        print(f"Age : {self.Age}")
        print(f"Marks : {self.Marks}")
    def calculate_grade(self):
        if self.Marks >=90:
            return "A"
        elif 80 <= self.Marks <= 89:
            return "B"
        elif 70 <= self.Marks <= 79:
            return "C"
        elif 60 <= self.Marks <= 69:
            return "D"
        else:
            return "E"

obj1 = Student("Jyothsna", 25, 84)
obj1.display()
print(f"Grade:{obj1.calculate_grade()}")
