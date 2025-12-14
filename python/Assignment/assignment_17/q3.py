# Create a class MedicalStudent inherited from Student with following : 
    # a. Data members :
        # i.Specialization 
        # ii.MarksOfInternship  
    # b. Add the following methods : 
        # i.Parameterized constructor 
        # ii.Display 
        # iii.Accept 
        # iv.override Method CalculateRank
        # v.Override __str__ Method

from q1 import Student

class MedicalStudent(Student):

    def __init__(self, student_id, name, age, percentage,
                 specialization, marks_of_internship):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

    # Accept method (overrides super)
    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marks_of_internship = float(
            input("Enter Marks of Internship: ")
        )

    # Display method (overrides super)
    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Marks of Internship:", self.marks_of_internship)

    # CalculateRank method (override super)
    def calculateRank(self):
        avg = (self.percentage + self.marks_of_internship) / 2

        if avg >= 75:
            return "Distinction"
        elif avg >= 60:
            return "First Class"
        elif avg >= 50:
            return "Second Class"
        elif avg >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__ method
    def __str__(self):
        return (f"StudentId: {self.student_id}, "
                f"Name: {self.name}, "
                f"Age: {self.age}, "
                f"Specialization: {self.specialization}, "
                f"Percentage: {self.percentage}, "
                f"Internship Marks: {self.marks_of_internship}, "
                f"Rank: {self.calculateRank()}")
    
m1 = MedicalStudent(0, "", 0, 0.0, "", 0.0)
m1.accept()
print("------------------------------------")
m1.display()
print("------------------------------------")
print("Rank:", m1.calculateRank())
print("------------------------------------")
print(m1)



 
