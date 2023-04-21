# make a two player rock paper scissors game

def rock_paper_scissors(choice_one, choice_two):
    while choice_one == choice_two:
        print("You tie")
        break
    if choice_one not in ("rock", "paper", "scissors"):
        print("%s has entered an invalid input" % user_one)
    elif choice_two not in ("rock", "paper", "scissors"):
        print("%s has entered an invalid input" % user_two)
    elif (choice_one == "rock"):
        if(choice_two == "paper"):
            print("%s, won this round" % user_two)
        elif(choice_two == "scissors"):
            print("%s, won this round" % user_one)   
    elif(choice_one == "paper"):
        if(choice_two == "rock"):
            print("%s, wins this round" % user_one)
        elif(choice_two == "scissors"):
            print("%s, wins this round" % user_two)
    elif (choice_one == "scissors"):
        if(choice_two == "rock"):
            print("%s, wins this round" % user_two)
        elif(choice_one == "paper"):
            print("%s, wins this round" % user_one)
    
        
user_one = input("User one, what is your name: ")
user_two = input("User two, what is your name: ")

print(user_one)
print(user_two)

choice_one = input("%s, do you want to pick rock, paper or scissors: " % user_one)
choice_two = input("%s, do you want to pick rock, paper or scissors: " % user_two)

rock_paper_scissors(choice_one, choice_two)

# comp versus user
import random

def user_v_comp(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("You choose", user_choice)
    print("Computer chose", computer_choice)
    
    if(user_choice == computer_choice):
        print("You tie")
        return
    elif user_choice not in ("rock", "paper", "scissors"):
        print("User has entered an invalid input")
    elif (user_choice == "rock"):
        if(computer_choice== "paper"):
            print(" Computer won this round")
        elif(computer_choice == "scissors"):
            print("User won this round")   
    elif(user_choice == "paper"):
        if(computer_choice== "rock"):
            print("User wins this round")
        if(computer_choice== "scissors"):
            print("Computer wins this round")
    elif (user_choice == "scissors"):
        if(computer_choice == "rock"):
            print("Computer wins this round")
        elif(computer_choice == "paper"):
            print("User wins this round")

user_choice = input("Choose between rock, paper, and scissors: ")
user_v_comp(user_choice)
    



