import random

RandomNumber=random.randrange(1,200)
print(RandomNumber)

userInput=int(input("Guess the number :"))

if userInput>RandomNumber:
    print(RandomNumber)
    print("The number is too high.")
elif RandomNumber>userInput:
    print(RandomNumber)
    print("The number is too low.")
else:
    print(RandomNumber)
    print("YES,Your number is Matched")    
        