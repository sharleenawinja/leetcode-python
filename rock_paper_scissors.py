# make a two player rock paper scissors game

def rock_paper_scissors(choice_one, choice_two):
    while choice_one == choice_two:
        print("You tie")
    if (choice_one == "rock"):
        if(choice_two == "paper"):
            print("%s, won this round" % user_two)
        else:
            print("%s, won this round" % user_one)   
    elif(choice_one == "paper"):
        if(choice_two == "rock"):
            print("%s, wins this round" % user_one)
        else:
            print("%s, wins this round" % user_two)
    elif (choice_one == "scissors"):
        if(choice_two == "rock"):
            print("%s, wins this round" % user_two)
        else:
            print("%s, wins this round" % user_one)
    else:
        print("Enter a valid input")
        
user_one = input("User one, what is your name: ")
user_two = input("User two, what is your name: ")

print(user_one)
print(user_two)

choice_one = input("%s, do you want to pick rock, paper or scissors: " % user_one)
choice_two = input("%s, do you want to pick rock, paper or scissors: " % user_two)

rock_paper_scissors(choice_one, choice_two)


