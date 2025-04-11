#Tuple
"""tuple are used to store multiple
items in single variable. A tuple is a 
collection which is ordered and unchangeable"""
#Tuples are written wtih round brackets.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Python-Update Tuples
y=list(thistuple)
y[1]="kiwi"
x=tuple(y)
print(x)
print("")
#ADD Items
"""Since tuples are immutable, they do not have a built-in append() method, but there are 
other ways to add items to a tuple.
1. Convert into a list: Just like the
workaround for changing a tuple, you can convert it into a list, add your item(s),
and convert it back into a tuple."""
#Convert the tuple into a list, add "orange", and convert it back into a tuple
y.append("orange")
x=tuple(y)
print(x)
"""2. Add tuple to a tuple. You are allowed to add tuples to tuples,
so if you want to add one item, (or many), create a new tuple with the item(s),
and add it to the existing tuple:"""
z=("orange",)
thistuple +=z
print(thistuple)
print("")
#Remove items from Tuple data type
"""Tuples are unchangeable, so we cannot remove items from it, 
but you can use the same workaround
as we used for changing and adding tuple items:"""
y=list(thistuple)
y.remove("banana")
x=tuple(y)
print(x)
print("")