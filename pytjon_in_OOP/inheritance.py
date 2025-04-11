class Calculator:
    '''Do addition,subtraction, multiplication and division '''
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "It is impossible to divide by Zero."

class SuperCalculator(Calculator):
    '''Child class of Calculator. Do square and cube.'''
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a

my_calculator=SuperCalculator()

temp=my_calculator.addition(23,47)
print(temp)

temp=my_calculator.subtraction(87,54)
print(temp)

temp=my_calculator.multiplication(65,56)
print(temp)

temp=my_calculator.division(852,76)
print(temp) 

temp=my_calculator.square(7)
print(temp)

temp=my_calculator.cube(3)
print(temp)
print( )
'''। এরর হ্যান্ডলিং চাপ্টারে আমরা বলেছিলাম পরে একসময় আমরা 
এই জিনিসটা শিখব। এখন সে সময় উপস্থিত। পাইথনে ইউজার 
ডিফাইন্ড এক্সেপশন প্রত্যক্ষ বা পরোক্ষভাবে Exception ক্লাস থেকে
ডিরাইভ (derive) করতে হবে'''

class CustomError(Exception):
    '''Just for example.'''
    def __init__(self,message):
        self.message=message

try:
    raise CustomError('It is a Custom Error.')
except CustomError as e:
    print(e)
print()
'''মেথড ওভাররাইডিং #
মেথড ওভাররাইডিং (overriding) একটা চমৎকার জিনিস। চাইল্ড ক্লাসে 
আমরা প্যারেন্ট ক্লাসের মেথডকে ওভাররাইড করে ঢেলে 
সাজাতে পারি। একেই মেথড ওভাররাইডিং বলে।'''
class Calculator:
    '''Do addition,subtraction, multiplication and division '''
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "It is impossible to divide by Zero."
class SuperCalculator(Calculator):
    '''do addition, subtraction,multiplication,division,square and cube'''
    def addition(self,a,b,c):
        return a+b+c
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a
    
my_calculator=SuperCalculator()
print(my_calculator.addition(23,47,12))
print(my_calculator.subtraction(87,54))
print(my_calculator.multiplication(65,56))
print(my_calculator.division(852,76))
print(my_calculator.square(7))
print(my_calculator.cube(3))
print()
""" এবার বাড়ির কাজ। ক্লাস কন্সট্রাক্টর __init__() কে ওভাররাইড করে একটা সুপারক্যালকুলেটর ক্লাস বানিয়ে প্রোগ্রাম লিখতে হবে।
পারা যাবে তো? অবশ্যই। কারণ, মানুষ আমাদের পাশে আছে।"""
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return 'It is impossible to divide by Zero.'

class SuperCalculator(Calculator):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def addition(self):
        return self.a +self.b+self.c
    def square(self):
        return self.a*self.a
    def cube(self):
        return self.a*self.a*self.a
    
my_calculator=SuperCalculator(12,13,14)
print(my_calculator.addition())
print(my_calculator.subtraction())
print(my_calculator.multiplication())
print(my_calculator.division())
print(my_calculator.square())
print(my_calculator.cube())

        