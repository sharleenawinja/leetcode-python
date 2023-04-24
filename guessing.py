# generate a random number between 1 and 9(including 1 and 9)
# ask the user to guess the number then tell them whether they guessed too low, too high or exactly right
# keep the game going until the user types exit
# keep track of how many guesses the user has made and when the game ends print this out

import random

def guessNumber(user_guess, random_number):
    global guesses
    if random_number == user_guess:
        print("You guessed right")
        print(f"You made {guesses} guesses")
    elif user_guess < random_number:
        print("low")
        next_trial= input("Enter another number or 'exit' to quit: ")
        if next_trial == "exit":
            print(f"You made {guesses} guesses")
            print("Exiting the game...")
            return
        else:
            guesses += 1
            next_guess = int(next_trial)
            guessNumber(next_guess, random_number)
    else:
        print("high")
        next_trial= input("Enter another number or 'exit' to quit: ")
        if next_trial == "exit":
            print(f"You made {guesses} guesses")
            print("Exiting the game...")
            return
        else:
            guesses += 1
            next_guess = int(next_trial)
            guessNumber(next_guess, random_number)

user_guess = int(input("Enter a number: "))
random_number = random.randint(1, 9)
guesses = 1
print(random_number)
guessNumber(user_guess, random_number)





