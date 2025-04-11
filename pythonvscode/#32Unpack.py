#Unpack Tuples in python
"""When we create a tuple,
we normally assign values to it. 
This is called "packing" a tuple:"""
fruits=("apple","banana", "cherry","angur")
a,b,c,d=fruits
print(d,a,b)
(g,*t,f)=fruits
print(g,t,f)
"""But,in python , we are also allowed to extract the values
back into variables. this is called "unpacking:"""
#Unpacking a tuple:
name=("math","physics","chemistry","biology","bangla")
(ath,hysics,hemistry,iology,angla)=name
print(iology)
""" The number of variables must match the number of 
values in the tuple, if not, you must use an
asterisk to collect the remaining values as a list."""
#using Asterisk
"""If the number of variables is less than the number
of values, you can add an * to the variable name and the 
values will be assigned to the variable as a list:"""
Fruit=("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=Fruit
print(green,yellow,red)
"""If the asterisk is added to another variable name than 
the last, Python will assign values to the variable until the number
of values left matches the number of variables left."""
fruits1=("apple","mango","papaya","pineapple","cherry")
(green,*tropic,red)=fruits1
print(tropic,red,green)