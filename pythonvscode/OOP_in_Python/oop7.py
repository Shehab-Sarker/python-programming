'''
del keyword
used to delete object properties or object itself
del s1.name
del s1
'''
class Student:
    def __init__(self,name):
        self.name=name
        
        
s1=Student("Shehab")
print(s1.name)
# del s1.name
# print(s1.name)        
print('')

