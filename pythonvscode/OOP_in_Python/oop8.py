''''
Private(like) attributes & methods
Conceptual Implementations in Python
Private attributes & methods are 
meant to be used only
within tha class and are not
accessible from outside the class
'''
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)
        # print(self.acc_no)    
        
acc1=Account("12345","abcde")
print(acc1.acc_no)
acc1.reset_pass()
print(acc1.reset_pass())
print('')


class Person:
    __name="Anonymous"
    
    def print_nam(self):
        print("Hello person") 
        print(self.__name)   
    
    
p1=Person()
# print(p1.__name) 
p1.print_nam()