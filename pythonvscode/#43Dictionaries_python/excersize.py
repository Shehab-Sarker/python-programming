student={
    "Name":"Shehab Sarker",
    "Class":"3rd Semister student",
    "Roll":"210346",
    "Number":1716416218,
    "Location":"Rajshahi",
    "Study":"Dept. of CSE,RUET",
}
print(student)
print("")
#clear() Removes all the elements from the dictinary
# student.clear()
# print(tudent)

#Copy() Returns a copy of the dictionary
std=student.copy()
for x,y in std.items():
    print(x,":",y)
print("")

#The fromkeys() method returns a dictionary with the specified keys and the specified value.
x=("key1","key2","key3")
# y=(1,2,3)
# newdic=dict.fromkeys(x,y)
newdic=dict.fromkeys(x)
print(newdic)
print("")

#The get() method returns the value of the item with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(car)
print(x)
print("")

#The items() method returns a list containing a tuple for each value key pair
print(student.items())
print('')

#the keys() method a list containing the dictionary's keys
print(student.keys())
print("")

#The  Pop() method remves the element with the specifies key
student.pop("Study")
print(student)
x=student.pop("Roll")
print(x)
print('')

#the popitem() Removes the last inserted key_value pair
print(student.popitem())
print(student)
print()

#The Update() method Updates the dictionary with the specified key_value pairs
student.update({ "school":"Komorpur High School"})
print(student)
print(student.values())
print('')

#The setdefault() method returns the value of the item with the specified key
