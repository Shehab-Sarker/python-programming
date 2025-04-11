#Accessing Items
#we can access the items of a dictionary by
# referring to its key name, inside square brackets
thisdict={
    "Name":"Shehab",
    "Age":25,
    "Country":"Banglasesh",
    "City":"Rajshahi",
    "University":"RUET"
}
x=thisdict["University"]
print(thisdict)
print("University Name:",x)
print("")
#There is also method called get() that will give our the same result:
y=thisdict.get("Name")
print("Name:",y)
print('')

#the keys() method will return a list of all the keys in the dictinary.
z=thisdict.keys()
print("ALL list Key:",z)
print('')
"""The list of the keys is a view of the dictionary, meaning that
any changes done to the dictionary will be reflected in the keys list."""
car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
xx=car.keys()
#before the change
print(car)
print("car key list:",xx)
car["color"]="white"
#After the change
print("Update key list:",xx)
print(car)
print("")

#The values method will return a list of all the values in the dictionary.
xn=thisdict.values()
print("all list value:",xn)
xn2=car.values()
print("ALL list value for car:",xn2)
print('')

#The list of the values is a view of the dictionary, meaning that any changes done to the 
# dictionary will be reflected in the values list
car["year"]=20933
#after the change
print("Update the list value:",xn2)
#Add a new item to the original dictionary, and see that the values list gets updated as well:
car["malik"]="shehab"
print("add the value:",xn2)
print(car)
print('')

#The items() method will return each item in a dictionary ,as tuples in a list
print(thisdict.items())
print(car.items())
print('')

#check if key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
if "Name" in thisdict:
    print("Yes,'Name' is one of the keys in the dictionary ")
    
    
"""Python Collections (Arrays)
There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""

