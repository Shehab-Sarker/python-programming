# Sequence type data type
"""Square Brackets []
parentheses()
curly brackets {}"""
# Type: list,tuple,range
"""List data type: The list is a data type that is mutable
Once a list has been created: Elements can be modified. Individual 
value can be replaced and List data type are immutable"""
lst=["Shehab","Sarker","Riat","Rahim","Karim","JObbar","Gaffar"]
print(lst)
lst[2]="Mahi Abdullah"
print(lst)
print(type(lst))
print("")

# Tuple data type
# Tuple data type are immutable

tup=(12,34,56,78,90)
print(tup)
tup1=("apple","Orange","lichi","Jackfruit","Black berry")
print(tup1)
print(type(tup))
print(" ")

# range data type
ren=range(6)
print(ren)
print(type(ren))

for i in ren:
    print(i)


#dict data type
x=dict(name="john",age=36)
#display x:
print(x)
#display the data type of x
print(type(x))