#python function
"""The following are the different types of python function:
Python Built_in Functions
Python Recursion Functions
python Lambda functions
Python User_defined Functions"""

def HabluFun(a,b):
    sum=a+b
    print("The sum:",sum)
  
def minusFun(a,b):
    sum=a-b
    print("The Subtraction:",sum)    
HabluFun(33,46)
minusFun(35,13)  
print('')
def my_function():
    print("Hello from a function") 
my_function()     
print('')

"""Arguments
Information can be passed into functions as arguments.Arguments are specified after the function
name, inside the parentheses. We can add as many arguments as we want, just separate them 
with a comma.The following example has a function with one argument (fname). When the function 
is called,we pass along a first name, which is used inside the function to print the full name:"""
def my_function(fname):
    print(fname +" Refsnes")
    
my_function("Emil")
my_function("Linus")    
print("")

"""Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before
the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:"""
def my_function2(*kids):
    print("The youngest child is "+ kids[2])

my_function2("Emil","Tobias","Linus")  

def my_function3(child3,child2,child1):
    print("The youngest child is "+child2)

my_function3(child1="Emil",child3="Tobias",child2="Linus")    
print('')    

"""Default Parameter Value
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:"""
def my_function4(country="ksaljf"):
    print("I am from "+country)

my_function4("Bnagladesh")    
my_function4("india")    
my_function4()    
my_function4("Brazil")    
print("")
"""Passing a List as an Argument
You can send any data types of argument to
a function (string, number, list, dictionary etc.),
and it will be treated as
the same data type inside the function."""    
def my_function6(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function6(fruits)    
print('')

"""Return Values
To let a function 
return a value, use the return statement"""
def my_function7(x):
    return 5*x

print(my_function7(3))
print(my_function7(9))
print(my_function7(6))
print('')
def my_function8(x):
  print(x)

my_function8(x=3)
print('')

"""Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.
Any argument before the / , are positional-only,
and any argument after the *, are keyword-only."""
def my_function9(a,b,/,*,c,d):
    print(a+b+c+d,a,b,c,d)
my_function9(3,4 ,c=7,d=8)    
    