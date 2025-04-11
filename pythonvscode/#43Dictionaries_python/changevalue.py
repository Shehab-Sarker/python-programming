#Change Values
#we can change the value of a specific item by referring to its key name:
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print("before Change:",thisdict)
thisdict["year"]="2018"
print("After change:",thisdict)
print("")

#Updae Dictionary
#The update() method will update the dictionary with
# the items from the given argument
#The argument must be a dictionary, or an iteraable object with key:value pairs.
thisdict.update({"model":"apple"})
print(thisdict)