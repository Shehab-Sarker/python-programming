#pyhon loops
#python has two primitive loop commands:
#while loops
#for loops
#The While loop
#With the while loop we can excute a set of statements as long as a condition is true
i=1
while i<6:
    print(i)
    i+=1
print('')

#With the break statement we can stop the loop even if the while condition is true:
j=1
while j<6:
    print(j) 
    if j==3:
        break
    j+=1
    
print("")
#With the continue statement we can stop the current iteration , and continue with nest:
i=0
while i<6:  
    i+=1  
    if i==3:
        continue
    print(i)
print('') 
   
"""The else Statement
With the else statement we can run a block of code once when the condition no longer is true"""
i=1
while i<6:
    print(i)
    i+=1
else:
    print(f"{i} is no longer than 6")
print("")

#For loops
#A for loop is used for iterating over a sequence 
#that is eaither a list,a tuple, a dictionary, a set, or a string 
fruits=["apple","banana","cherry"]

for n in fruits:
    if n=="banana":
        continue
    print(n)

print('')
for x in range(2,6):
    print(x)  
print('')
#The range() function defaults to increment the sequence by 1, however it is possible to
# specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2,30,9):
    print(x)      
else:
    print("Finally FInished") 
print("")

for x in range(6):
    if x==3:
        break
    print(x)  
else:
    print("Finally finished")    
print('')
#Nested loops
"""A nested loop is a loop inside a loop.
The "inner loop" will be executed one time 
for each iteration of the "outer loop"""
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]      

for x in adj:
    for y in fruits:
        print(x,y)