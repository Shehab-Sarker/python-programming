#List Comprehension
"""List comprehension offers a shorter syntax when you want to create a new list based 
on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" 
in the name.Without list comprehension you will have to write a for statement with a 
 conditional test inside:"""
fruits=["apple","banana","cherry","kiwi","mango"]
print("Fruits:",fruits)
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print("newlist:",newlist) 
print("")

# With list comprehension you can do all that with only one line of code
newlist1=[x for x in fruits if "e" in x]
print("newlist1:",newlist1)
print("")

#The Syntax
"""newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged
The condition is like a filter that only accepts the items that valuate to True.
The condition if x != "apple"  will return True for all elements other than "apple", making
the new list contain all fruits except apple"""
newlist3=[x for x in fruits if x!="apple"]
print("newlist3",newlist3)
print("")
#iteraable can be any iterable object ,like a list
#tuple,set etc
newlist4=[t for t in range(10)]
print("Newlist4:",newlist4)
newlist5=[t for t in range(10) if t<6]
print("Newlist5:",newlist5)
print("")
#Expression
"""The expression is the current item in the iteration, but it is
also the outcome, which you can manipulate 
before it ends up like a list item in the new list:"""
#Set the values in the new list to upper case:
newlist6=[x.upper() for x in fruits]
print("newlist6:",newlist6)
print("")
#Set all values in the new list to 'hello':
newlist7=["hello" for d in fruits]
print("newlist7:",newlist7)
print("")
"""The expression can also contain conditions, not like a filter,
but as a way to manipulate the outcome:"""
newlist8=[x if x!="banana" else "orange" for x in fruits ]
print("newlist8:",newlist8)

print("")
newlist9=[x if x=="banana" else "orange" for x in fruits ]
print("newlist9:",newlist9)

print("")

#list comprehension 
num=[1,2,3,4,5,6,7]
for i in num:
    print(i*2)
num1=[x*2 for x in num]
print("num1:",num1)
print("")
num2=[]
for i in num:
    num2.append(i*3)
print("num2:",num2)
print("")