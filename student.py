class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

Student = Student("Jyothsna",25)
Student.display()
