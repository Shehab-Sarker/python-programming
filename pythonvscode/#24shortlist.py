#Sort list Alphanumerically
"""List objects have a sort() method that will sort the list
alphanumerically, ascending, by default:"""
country=["zimbabua","india","banglasesh","srilanka","pakistan"]
country.sort()
print("Sort:",country)
print("")
numlist=[123,354,25,75,252]
numlist.sort()
print("Sort assending",numlist)
print("")
#Sort Descending
"""to sort descending , use the 
keyword argument reverse = true"""
country.sort(reverse=True)
print("Sort decending:",country)
numlist.sort(reverse=True)
print("Sort descending:",numlist)
print("")

#Customize sort Function
"""You can also customize your own function by using the
keyword argument key = function.
The function will return a number that will be 
used to sort the list (the lowest number first):"""
def myfunc(n):
    return abs(n-50)

numlist.sort(key=myfunc)
print("Customize sort fumction abs(n-50)",numlist)
print("")
#Case sensitive sorting can give unexpected result:
country2=["bangladesg","Zinbabua","afganistan","Austrilia","Pakistan","srilanka"]
country2.sort()
print("Case insensitive Sort:",country2)
print("")

"""Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, 
use str.lower as a key function:"""
country2.sort(key=str.lower)
print("Case insensitive ascending sort:",country2)
print("")

#Reverse Order
"""What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements"""
country2.reverse()
print(country2)
numlist.reverse()
print(numlist)
print("")

eng=["r","y","w","d","h","a","s","p"]
eng.sort()
print("Sorting Ascending:",eng)
eng.reverse()
print("Sorting Ascending:",eng)