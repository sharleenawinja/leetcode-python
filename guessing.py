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

user_guess = int(input("Enter a number between 1 and 9: "))
random_number = random.randint(1, 9)
guesses = 1
print(random_number)
guessNumber(user_guess, random_number)

# import random

def guess_number():
    random_number = random.randint(1, 9)
    num_guesses = 0
    while True:
        user_guess = input("Guess a number between 1 and 9 (or type 'exit' to quit): ")
        if user_guess.lower() == "exit":
            print(f"You made {num_guesses} guesses.")
            print("Exiting the game...")
            break
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9 (or type 'exit' to quit).")
            continue
        num_guesses += 1
        if user_guess == random_number:
            print("Congratulations, you guessed the number!")
            print(f"You made {num_guesses} guesses.")
            break
        elif user_guess < random_number:
            print("Too low! Guess again.")
        else:
            print("Too high! Guess again.")

guess_number()





