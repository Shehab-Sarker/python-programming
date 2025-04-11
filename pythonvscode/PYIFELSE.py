#pythone if-else conditions and if state ments
a=27
b=200
if b>a:
    print(f"{b} is greater than {a}")
elif a==b:
    print(f"{a} and {b} are equal")    
else:
    print(f"{a} is greater than {b}")  
print('')

x=23
y=34
if x>y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is not grater than {y}")   
print('') 

#short hand if
if y>x : print(f"{y} is greater than {x}")
print('')
#one line if else staement
print(f"{a} greater than {b}") if a>b else print(f"{b} grater than {a}")       
print('')

#one line if else statement , with 3 conditions
s=46
r=46
print("S") if s>r else print("R") if r>s else print("Equal")             
print('')

#AND : The and keyword is a logical opeartor , and is used to combine conditional statements:
a=200
b=33
c=500
if a>b and c>a:
    print("Both conditions are true")
else:
    print("One of the conditions are false")   
print("")

#the or keyword is a logical operator , and is used to combine conditional statements:
if a>b or a>c:
    print("At least one of the condition is true")
print("")

#The Not keyword is a logical operator ,and is used to reverse the result of the conditinal statements:
a=33
b=200
if not a>b:
    print(f"{a} is not greater than {b}")        
    
print('') 

#Nested If 
x=16    
if x>10:
    print("Above ten,")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20")   
print("")
a=33
b=200
if b>a:
    pass