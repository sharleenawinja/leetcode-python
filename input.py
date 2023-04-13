# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

name = input("What is your name: ")
age = int(input("How old are you: "))
year = 2023 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))

# creating a function
def hundredth_year(name, age):
    year = 2023 - int(age) + 100
    message = name + ", you will be a hundred years old in the year " + str(year)
    return message

name = input ("What is your name: ")  
age = input("How old are you: ")
message = hundredth_year(name, age)
print(message) 