#join Two tuples
#to join two or more tuples you can use the + operator:
tuple1=("a","b","c","d","e","f")
tuple2=(1,2,3,4,5,6)
tuple3=tuple1+ tuple2
print(tuple3)
tuple1+=tuple2
print(tuple1)
print("")

#Multiply Tuples
"""We want to multiply the content of 
a tuple a given number of times, we can use the * operator:"""
#Multiply the fruits tuple by 2:
fruits=("apple","banana","chery")
mytuple=fruits*2
print(mytuple)
print("")

fruits=["apple","banana","chery"]
mytuple=fruits*4
print(mytuple)