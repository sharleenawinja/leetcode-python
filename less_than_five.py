# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# def less_than_five(numList):
#     for num in numList:
#         if num < 5:
#             print(num)


# less_than_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

# extras
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# def list_of_less_than_five(numList):
#     less_than_five = []
#     for num in numList:
#         if num < 5:
#             less_than_five.append(num)
#     return less_than_five

# print(list_of_less_than_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))  

# doing it in one line
# using list comprehension
a = [1, 2, 3, 4, 5, 6, 7,]
print( [ x for x in a if x<5 ] )

# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# def less_than_num(numList, num):
#     less_than = []
#     for element in numList:
#         if element < num:
#             less_than.append(element)
#     return less_than 

# numInput = int(input("Enter any number: "))  
# print(less_than_num([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], numInput))         
