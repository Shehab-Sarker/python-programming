#Copy a list
"""You cannot copy a list simply by typing list2 = list1, because: 
list2 will only be a reference to 
list1, and changes made in list1 will automatically also be made in list2.
There are ways to make a copy,
one way is to use the built-in List method copy()."""
list1=["alu","potol","begun","tomato","shosha","piaz","rosun"]
print("List1:",list1)
# list2=list1
list2=list1.copy()
print("List2 copy from list1:",list2)
print("")

#Another way to make a copy is to use the built-in method list().
#Make a copy of a list with the list() method:
list3=list(list1)
print("list3 copy the list() method:",list3)
print('')

num=[1,2,3,4,5]
num1=num.copy()
print(num1)
print('')

#Python list count() Method
"""Return the number of times the value "cherry" 
appears in the fruits list:"""
fruits=["apple","banana","cherry"]
x=fruits.count("apple")
print("apple count:",x)
print('')
#Python List index() Method 
x1=fruits.index("banana")
print("banana position:",x1+1)