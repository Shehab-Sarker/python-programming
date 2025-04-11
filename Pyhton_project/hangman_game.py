word ="Hablu"
chances = 5
GuessAdd=[]
done = False

while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter,end=" ")
        else:
            print("_",end="")
    MyGuess = input(f"Your Changes is : {chances}, Guess The letter: ")
    GuessAdd.append(MyGuess.lower())
    if MyGuess.lower() not in word.lower():
        chances-=1
        if chances==0:
            break      
    
    done = True     
    for letter in word:
        if letter.lower() not in GuessAdd:
            done=False
            
if done:
    print(f"yes, you have won the game,the word is {word} ")
else:
    print(f"no,You loss the game,the word was {word}. ")                
            
            
                