# Ask the user for a number and determine whether the number is prime or not.
# prime number =. a whole number greater than 1 that cannot be divided by any whole number other than itself

def is_prime(num):
    # check if num is less than 2 which is not a prime number
    if num < 2:
        print(f"{num} is not a prime number")
        exit()  #exit the program early

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
