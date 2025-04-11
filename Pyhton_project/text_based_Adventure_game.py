answer=input("Do you want to play this game? [Yes/No] : ")

if answer=="Yes":
    print("Welcome to the game!")
    answer=input("Do you want to go Jungle or Cave? [Jungle/Cave] : ")
    if answer=="Jungle":
        print("You are see the hungry  Tiger 😢. TIger will eat you. So,game are Closed")
    elif answer=="Cave":
        print("You are seen the bear in front of Cave.")
        answer=input("Do you want to fight with the bear or run away! [fight/run] : ")
        if answer=="fight":
            print("Bear is too much Strong! You are loss the game!")
        else:
            print("Wow! still you are alive🙂!")  
            
else:
    print("Please play this game at least 1 time.")
    print("The Game is Closed. Thanks for Playing")
        
