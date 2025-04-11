#Python Set copy() Method
fruits={"apple","banana","cherry"}
x=fruits.copy()
print(x)
#The copy() method copies the set.
print('')

#Python Set difference() Method
#Return a set that contains the items that only
# exist in set x, and not in set y
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.difference(y)
r=y.difference(x)
print(z)
print(r)
print("")
""""Definition and Usage
The difference() method returns a set that contains the difference between two sets.
Meaning: The returned set contains items that 
exist only in the first set, and not in both sets."""
x.difference_update(y)
print(x)
"""Definition and Usage
The difference_update() method removes the items that exist in both sets.
The difference_update() method is different from the difference() method, because the difference() method 
returns a new set, without the unwanted items, and the difference_update() 
method removes the unwanted items from the original set."""
print("")

#Python Set isdisjoint() Method
#Return True if no items in set x is present in set y:
x1={"apple","banana","cherry"}
y1={"google","microsoft","facebook"}
z1=x.isdisjoint(y)
print(z1)

"""Definition and Usage
The isdisjoint() method returns True
if none of the items are present in both sets, 
otherwise it returns False."""
"""What if no items are present in both sets?
Return False if one or more items are present in both sets:"""
y3={"google","microsoft","apple"}
z13=x1.isdisjoint(y3)
print(z13)
print('')

#Python Set issuperset() Method
#Return True if all items set y are present in set x:
x5={1,2,3,4,5,6}
y5={6,5,4}
z5=x5.issuperset(y5)
print(z5)
print('')
#The issuperset() method returns True if all items in the specified set exists in
# the original set, otherwise it returns False.

t={6,5,10}
re=x5.issuperset(t)
print(re)