#Join Two Sets
"""There are several ways
to join two or more sets in Python.
You can use the union()
method that returns a new set containing all 
items from both sets, or the update() method that inserts all
the items from one set into another:"""
#The union() method returns a new set with all items from both sets:
set1={1,2,3,4,5}
set2={23,4,5,67,53}
set3={11,22,33,44,55}
set4=set1.union(set2)
print(set4)
set2.update(set3)
print(set2)
#Note: Both union() and update()
#will exclude any duplicate items

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.
x={1,2,3,4,"shehab",True,0,"Hridoy"}
y={3,8,9,7,"Hridoy",False,1,"Sarker"}
x.intersection_update(y)
print(x)
print('')

#The intersection() method will return a new set, that only contains
# the items that are present in both sets.
x1={1,2,3,4,"shehab",True,0,"Hridoy"}
y1={3,8,9,7,"Hridoy",False,1,"Sarker"}
tt=x1.intersection(y1)
print(tt)
print("")

#Keep All, But NOT the Duplicate
"""The symmetric_difference_update() method will keep only the elements
that are NOT present in both sets."""
x2={1,2,3,4,"shehab",True,0,"Hridoy"}
y2={3,8,9,7,"Hridoy",False,1,"Sarker"}
x2.symmetric_difference_update(y2)
print(x2)

#The symmetric_difference() method will return a new set, that contains only
#the elements that are NOT present in both sets.
x3={1,2,3,4,"shehab",True,0,"Hridoy"}
y3={3,8,9,7,"Hridoy",False,1,"Sarker"}
ss=x3.symmetric_difference(y3)
print(ss)