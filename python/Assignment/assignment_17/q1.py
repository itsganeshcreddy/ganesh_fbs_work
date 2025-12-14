# 1. Create a class Student with following  
    # a.data members: 
       # i.StudentId 
       # ii.Name
       # iii.Age 
       # iv.Percentage  
    # b. Add the following methods :
       # i.Parameterized constructor
       # ii.Display 
       # iii.Accept  
       # iv.Method CalculateRank  
       # v.Override __str__ Method  

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Percentage :", self.percentage)

    def calculateRank(self):
        if(self.percentage >= 75):
            return "Distinction"
        elif(self.percentage >= 50):
            return "First Class"
        elif(self.percentage >= 36):
            return "Second Class"
        else:
            return "Fail"

    # Override __str__ method
    def __str__(self):
        return (
            f"Student ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Percentage: {self.percentage}, "
            f"Rank: {self.calculateRank()}"
        )

# s1 = Student(101, "Ganesh", 21, 82.5)
# s1.display()
# # Print object (__str__ method)
# print(s1)
# print('*******************************************************************')

# s2 = Student(0, "", 0, 0.0)
# s2.accept()
# print('--------------------------------------------------------------------')
# s2.display()
# print(s2.calculateRank())
# print(s2)



 

