# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# a divisor is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def find_divisors(test_num):
    for num in range(1, test_num+1):
        if test_num % num == 0:
            print(num)


input_num = int(input("Enter any number: "))
find_divisors(input_num)

# second method
# using a list
num = int(input("Enter a number: "))

# Create an empty list to store divisors
divisors = []

# Iterate over all possible divisors from 1 to num
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

# Print the list of divisors
print("The divisors of", num, "are:", divisors)

