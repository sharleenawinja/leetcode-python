# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

def less_than_five(numList):
    for num in numList:
        if num < 5:
            print(num)


less_than_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

# extras
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
def list_of_less_than_five(numList):
    less_than_five = []
    for num in numList:
        if num < 5:
            less_than_five.append(num)
    return less_than_five

print(list_of_less_than_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))  

# doing it in one line
# using list comprehension
a = [1, 2, 3, 4, 5, 6, 7,]
print( [ x for x in a if x<5 ] )

# list comprehension is a concise way to create a new python list by iterating over an existing 
# sequence and applying a condition to each element of the sequence.
# It is written as a single line of code using a special syntax, and can include one or more 
# for loops and if statements

# The basic syntax of a list comprehension is:
# new_list = [expression for variable in sequence if condition]
# where 'expression' is an expression that is evaluated for each element in 'sequance', 'variable' 
# is a new variable that takes on the value of each element in 'sequance' as the loop iterates, 
# "sequance" is an existing sequance (eg a list or a string) and "condition" is an optional 
# condition that filters the elements of "sequence" that are included in the new list
# 

# For example the following code creates a list of the squares of the numbers 1 through 5
# using list comprehension:
squares = [x**2 for x in range(1, 6) ]

# this is equivalent to the following code using a "for" loop
squares = []
for x in range(1, 6):
    squares.append(x**2)

# the range() function returns a sequance of numbers starting from 0 by default, and incrementd by 1(by default), and stops before a specidied nunber



# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
def less_than_num(numList, num):
    less_than = []
    for element in numList:
        if element < num:
            less_than.append(element)
    return less_than 

numInput = int(input("Enter any number: "))  
print(less_than_num([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], numInput))         
