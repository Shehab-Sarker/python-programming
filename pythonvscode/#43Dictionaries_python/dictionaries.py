studentinfo={
    "Shehab":{
        "Location":"Rajshahi",
        "Study":"Dept. of CSE, RUET",
        "Subject":"Computer",
        "ROLL":2103046,
        "Number" : 1716416218,
    },
     "Sarker":{
        "Location":"Gaibandha",
        "Study":"Dept. of CSE, RUET",
        "Subject":"Computer",
        "ROLL":2103046,
        "Number" : 1947383480
    }
}
print(studentinfo)
print(studentinfo["Sarker"])
print(studentinfo["Sarker"]["Number"])
print(studentinfo["Sarker"]["Location"])
print("")
#Dictionary
"""Dictionaries are used to store data 
values in key:value pairs.
A dictionary is a collection which is ordered*, 
changeable and do not allow duplicates"""
#Dictionaries are written with curly brackets, and have keys and values:
print("Create and print a dictionary:")
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)
print('')
#Dictionary Items
"""Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and 
can be referred to by using the key name"""
print("Brand:",thisdict["brand"])
print('')
"""When we say that dictionaries are ordered, it means that the items have a defined order, 
and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index."""

#changable
"""Dictionaries are changeable, meaning that we can change, add or
remove items after the dictionary has been created"""
#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:
thisdict2={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "year":2020
}
print(thisdict2)