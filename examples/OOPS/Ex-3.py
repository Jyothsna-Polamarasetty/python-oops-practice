class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"name: {self.name}")
        print(f"id : {self.id}")
        print(f"salary :{self.salary}")
    def annual_salary(self):
        return self.salary * 12
    def give_bonus(self,bonus_percentage):
        new_salary = self.salary + self.salary * bonus_percentage/100
        self.salary = new_salary
        return self.salary
 
ji= Employee(123,"Jyothsna",90000)
ji.display_details()
print(ji.annual_salary())
print("new_slary is", ji.give_bonus(10))
