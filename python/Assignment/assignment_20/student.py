# Problem statement on containment 
    # Write a program to  
    # 1. create a package “SY” which has  class SYMARKS (Computer Total, MathsTotal, ElectronicsTotal).  
    # 2. Create another package “TY” which has a class TYMarks (Theory,Practical).  
    # 3. Create object of student class (Outside SY & TY package) having roll 
        # number, name, SYMakrs and TYMarks. Add the marksof SY and TY 
        # Computer subjects and calculate grade ("A" for >=70, "B" for >=60, 
        # "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result 
        # of the student in proper format.

from SY.symarks import Symarks
from TY.tymarks import Tymarks

class Student:
    def __init__(self, roll, name, sy_marks, ty_marks):
        self.roll = roll
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks
        
    def calculate_grade(self):
        total = self.sy_marks.computer + self.ty_marks.theory

        if(total >= 70):
            grade = 'A'
        elif(total >= 60):
            grade = 'B'
        elif(total >= 50):
            grade = 'C' 
        elif(total >= 40):
            grade = 'Pass Class' 
        else:
            grade = 'Fail' 

        print('Roll No :', self.roll)
        print('Name    :', self.name)
        print('SY Computer Marks :', self.sy_marks.computer)
        print('TY Computer Marks :', self.ty_marks.theory)
        print('Total Computer Marks :', total)
        print('Grade :', grade) 

sy = Symarks(45, 60, 55)               
ty = Tymarks(30, 25)

s1 = Student(101, 'Ganesh', sy, ty)
s1.calculate_grade()