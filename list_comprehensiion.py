# given a list saved in a variable eg a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
# write one line of python that takes this list and makes a new list that has only the even elements of this list in it

all_elements = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
even_elements = [x for x in all_elements if x%2 == 0 ] 
print(even_elements)

# the idea of list comprehension is to make code more compact to accomplish tasks involving lists
# compact code => doing things with the shortest line of code
# compact code means that the code is written in a coincise and efficient manner while still maintaining readability and clarity
# compact code is often achieved through the use of programming constructs such as functions loops and conditional statements to minimize repetition and maximize reusability
# compact code can offer several benefits such as:
#   1. reducing the overall length of the codebase
#   2. improving maintainability by making the code easier to read and understand 
#   3. reducing the likelihood of errors and bugs
# however it is important to strike a balance between compactness and readabiility; overly compact code can be difficult to understand and maintain, particularly for other developers who may be working on the same codebase
# in general, writing compact code is a goal for most software development projects, as it can lead to more efficient and effective development process
# however it is important to prioritize clarity and readability, particularly when working on large or complex projects


# SECOND EXAMPLE OF HOW LIST COMPREHENSION MAKES CODE MORE COMPACT
# code without list comprehension
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth:
    ages.append(2014 - year)
print("ages", ages)

# with list comprehension
list_of_ages = [2014 - year for year in years_of_birth]
print("list", list_of_ages)




