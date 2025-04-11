#LOOP Through a list
#we can loop through the list items by using a for loop:
mylist=["Dhakha","gaibandha","Rangpur","Rajshahi","Bogura","Cumilla"]
for x in mylist:
    print(x)
print("")  

#Loop through the Index numbers
"""We can also loop through the list items by
referring to their index number.
Use the range() and len() functions to create
a suitable iterable. the iterable created in the example above is [0,1,2]""" 
for i in range(len(mylist)):
    print(mylist[i])
print("")
for i in range(3):
    print(mylist[i])   
    
print("The length of list:",len(mylist))     
print("")
#Using a While Loop
"""we can loop through the list items by 
using a whie loop.Use the len() function to determine
the length of the list ,then start at 0 and loop your
way through thelist items by referring to their indexes .
remember to increase the index by 1 after each iteration"""
t=0
while t<6:
    print(mylist[t])
    t=t+1
print("")    

#Looping Using List Comprehansion
"""List Comprehension offers the shortest 
syntax for looping through lists"""
#A short hand for loop that will print all items in a list:
print("The length of list:",len(mylist))     
[print(x) for x in mylist]