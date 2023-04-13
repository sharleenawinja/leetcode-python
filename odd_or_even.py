# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

def even_or_odd(num): 
    if num % 2 == 0:
        print(str(num) + " is an even number")
    else:
        print(str(num) + " is an odd number")    

number = int(input("Enter any number: "))
even_or_odd(number)



