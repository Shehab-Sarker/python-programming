'''
Class method
A class method is bound to the class& receives
the class as an implict first argument

Note-static method can't access or modify class
state & generally for utility
class Student:
    @classmethod #decorator
    def college(cls):
        pass
'''
class Person:
    name="anonymous"
    
    # def changeName(self,name):
    #     self.name=name
    #     Person.name=name
    #     self.__class__.name="RAHUL"
    @classmethod
    def changeName(cls,name):
        cls.name=name
        
        
p1=Person()
print(p1.name)
p1.changeName("shehab sarker")
print(p1.name)
print(Person.name)   
print(p1.name)     

