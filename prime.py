# Ask the user for a number and determine whether the number is prime or not.
# prime number =. a whole number greater than 1 that cannot be divided by any whole number other than itself

def is_prime(num):
    # check if num is less than 2 which is not a prime number
    if num < 2:
        print(f"{num} is not a prime number")
        exit()  #exit the program early. exit is a built in python function that is used to terminate the program execution
        # when exit is called, the python interpreter will immediately stop executing the program and exit
        # exit is different from return which is used to exit a function and return a value
        # exit is used to exit the entire program while return is used to exit a function and return the value to the caller

    # check if the number is divisible by any number between 2 and num-1
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break #exit the loop early if the number is not prime

    #if we made it through the loop without finding a factor, the number is prime
    else:
         print(f"{num} is a prime number.")

user_num = int(input("Enter any number: "))
is_prime(user_num)

# second solution => using a flag variable
def prime_using_flag(num):
    if num < 2:
        print(f"{num} is not a prime number.")
        exit() 

    #set a flag variable to keep track of whether we've found a variable
    found_factor = False

    for i in range(2, num):
        if num % i == 0:
            found_factor = True
            break  
    
    # if we found a factor, the number is not prime
    if found_factor:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")


num = int(input("Enter a number: "))
prime_using_flag(num)


# all() function returns True if all items in an iterable are true, otherwise it returns false
# if the iterable object is empty the all() function returns true