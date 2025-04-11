#join twolist
num1=[2,4,5,6,7]
print("list extend before:",num1)
num2=[11,22,33,44,55]
num1.extend(num2)
print("list extend after:",num1)
print('')

"""There are several ways to join, or concatenate,
two or more lists in Python.
One of the easiest ways are by 
using the + operator."""
num3=["a","b","c","d","e"]
num4=num3+num2
print("Join by + oprator:",num4)
print('')

"""Another way to join two lists is by appending all the items
from list2 into list1, one by one:"""
for x in num1:
    num3.append(x)

print("join by apppend():",num3)

