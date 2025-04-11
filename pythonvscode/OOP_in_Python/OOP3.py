class Student:
    college_name="ABC Collage"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding a new student in database...")

s1=Student("Karan",97)        
print(s1.name)
print(Student.college_name)