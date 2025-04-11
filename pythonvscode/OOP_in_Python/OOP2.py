'''
__init__ function
Constructor 
ALL classes have a function called _init_(), which is always
executed when the class is being initiated.
#creating class
class Student:
    def __init__(self,fullname):
       self.name=fullname

#creating object       
s1=Student("Shehab Sarker")
print(s1.name)   


'The self parameter is a reference to the current
instance of the class , and is used to access variables 
that belongs to the class'    
'''

#creating class
class Student:
    #default constructor
    def __init__(self):
        pass
    
    #paramaterized constructor
    def __init__(self,name,marks):
       self.name=name
       self.marks=marks
       print("Adding a new a student in Database")

#creating object       
s1=Student("Shehab Sarker",99)
print(s1.name,s1.marks)  

s2=Student("mahi Abdullah",90)
print(s2.name,s2.marks) 