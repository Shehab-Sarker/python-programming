'''
Polymorphism: operator Overloading
When the same operator is allowed to have different
meaning according to the context
Operator & Dunder Functions
a+b #addition   a.__add__(b)
a-b #subtraction  a.__sub__(b)
a+b #multiplication   a.__mul__(b)
a+b #division   a.__truediv__(b)
a+b #mod   a.__mod__(b)
'''

# print("Apna"+"college")
# print([1,2,3]+[4,5,6])

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def shownumber(self):
        print(self.real,"i+",self.img,"j")
        
    # def add(self,num):
    def __add__(self,num):
        newreal=self.real+num.real
        newimg=self.img+num.img
        return Complex(newreal,newimg)
    def __sub__(self,num):
        newreal=self.real-num.real
        newimg=self.img-num.img
        return Complex(newreal,newimg) 
    
    # def __mul__(self,num):
    #     newreal=self.real-num.real
    #     newimg=self.img-num.img
    #     return Complex(newreal,newimg) 
    
    
    def __mul__(self,num):
        newreal=self.real*num.real
        newimg=self.img*num.img
        return Complex(newreal,newimg)   

num1=Complex(1,3)
num1.shownumber()        

num2=Complex(4,6)
num2.shownumber() 

# num3=num1.add(num2)
num3=num1+num2
num3.shownumber()

num3=num1-num2
num3.shownumber()  
num3=num1*num2
num3.shownumber()        
            
        