"""Lamda is keyword in Python for defining the anonymous function
arguments(s) is a placeholder,that is a variable that will be uesd 
to hold the value we wanr to pass into the function expression . A 
lambda function can have multiple variables depending on what you want to achieve"""
def hablufun(a,b):
    sum=a+b
    print(sum)
x=lambda a,b: a+b
print(x(50,10))
print("")

#A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression
x=lambda a:a+5
print(x(5))
print('')

#Lambda functions can take any number of arguments:
#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
    return lambda a:a*n


mytripler=myfunc(3)
print(mytripler(11))
