myset={"apple","banana","cherry"} #this is set data type method
print(myset)
print("")
#Set are written with curly brackets.
#SET
"""A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items."""
myset1={1,False,"string","string"}
print(myset1)
print(type(myset1))
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.
#Sets are unordered, so we are cannot be sure in which order the items will appear.
#set items
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset={"apple","banana","cherry",True,1,2}
print(thisset)
#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset2={"apple","banana","cherry",False,0,True,1,2,3}
print(thisset2)
print('')
#Get the length of set
#To determine how many items a set has, use the len() function.
print("the length of Thisset:",len(thisset))
#Set items -DataTypes
#set items can be of any data type:
set1={"apple","banana","cherry"}
set2={1,5,7,9,3}
set3={True,False,False}
print(set1,'\n',set2,'\n',set3)
#A set can contain different data types:
#A set with strings, integers and boolean values:
set4={"abc",34,True,40,"male"}
print(set4)
print(type(set1))
print('')

#the set() constructor
#it is also possible to use the set() constructor to make a set
thisset3=set(("apple","banana","cherry"))
#note the double round-brackets
print(thisset3)
# Note: the set list is unordered, so the result will display the items in a random order.

"""Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove items and add new items"""