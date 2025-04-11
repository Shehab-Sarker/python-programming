'''
Static Methods
Methods that don't use the self parameter (work at class)
class Student:
    @staticmethod #decorator
    def college();
        print("ABC College")
        
Decorators allow us to wrap another function in order to 
extend the behaviour of the wrapped function,
without permanently modifying it        
'''

class Student:
    college_name="ABC Collage"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("Hello") 
    def welcome(self):
        print("Welcome student.",self.name)
        
    def get_marks(self):
        return self.marks     
          
s1=Student("Karan",97)        
s1.welcome()
print(s1.get_marks()) 
s1.hello()
