import random

DiceRolling=True

while DiceRolling:
    print(random.randint(1,6))
    PlayAgain=input("Do you want to Roll Again? [yes/no] : ")
    if PlayAgain=="yes":
        continue
    else:
        print("Game over!")
        break