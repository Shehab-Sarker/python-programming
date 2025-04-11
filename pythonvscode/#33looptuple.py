#loop through a tuple
#we can loop through the tuples items by using a for loop
thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x)
print('')
#Loop through the index Numbers
"""WE can also loop through the tuples items by 
referring to index number
Use the range() and len() functions to create a suitable iterartable"""
for i in range(len(thistuple)):
    print(thistuple[i])
print('')

#Using a while loop
#We can loop through the tuple items by using a while loop
"""Use the len() function to determine the length of the tuple, then start at 0 and loop your way 
through the tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration."""
i=0
while i<len(thistuple):
    print(thistuple[i])
    i+=1
print('')
