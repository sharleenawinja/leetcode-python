# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

def even_or_odd(num): 
    if num % 2 == 0:
        print(str(num) + " is an even number")
    else:
        print(str(num) + " is an odd number")    

number = int(input("Enter any number: "))
even_or_odd(number)

# extras
# If the number is a multiple of 4, print out a different message.
def even_or_odd_or_multiple_of_four(num):
    if num % 4 == 0:
        print(str(num) + " is a multiple of 4")
    elif num % 2 == 0:
        print(str(num) + " is an even number")
    else:
        print(str(num) + " is an odd number")   

testnum = int(input("Enter any number: "))  
even_or_odd_or_multiple_of_four(testnum)    

# more extras
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
def divide_evenly(num, check):
    if num % check == 0:
        print(str(check) + " divides " + str(num) + " evenly" )
    else:
        print(str(check) + " does not divide " + str(num) + " evenly")  

num_to_divide = int(input("Enter any number: "))    
num_to_be_divided = int(input("Enter another number: "))   
divide_evenly(num_to_be_divided, num_to_divide)   

