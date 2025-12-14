# 2.Create a derived class from Student as EnggStudent with : 
    # a.Data members as :  
       # i.Branch 
       # ii.InternalMarks  
    # b. Add the following methods : 
       # i.Parameterized constructor 
       # ii.Display 
       # iii.Accept 
       # iv.override Method CalculateRank 
       # v.Override __str__ Method

from q1 import Student

class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    # Accept method (overrides super)
    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internal_marks = float(input("Enter Internal Marks: "))

    # Display method (overrides super)
    def display(self):
        super().display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internal_marks)

    # CalculateRank method (override super)
    def calculateRank(self):
        avg = (self.percentage + self.internal_marks) / 2

        if(avg >= 75):
            return "Distinction"
        elif(avg >= 60):
            return "First Class"
        elif(avg >= 50):
            return "Second Class"
        elif(avg >= 35):
            return "Pass"
        else:
            return "Fail"

    # Override __str__ method
    def __str__(self):
        return (f"StudentId: {self.student_id}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Branch: {self.branch}, "
                f"Percentage: {self.percentage}, "
                f"Internal Marks: {self.internal_marks}, "
                f"Rank: {self.calculateRank()}")
    
e1 = EnggStudent(0, "", 0, 0.0, "", 0.0)
e1.accept()
print("------------------------------------")
e1.display()
print("------------------------------------")
print("Rank:", e1.calculateRank())
print("------------------------------------")
print(e1)


