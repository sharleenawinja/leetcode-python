# SLICING
# in python, a list is a collection of ordered elements
# list slicing is a way to extract a subset of elements from a list by specifying a range of indices
# list slicing is done through a colon operator
# the sytax for list slicing is as follows
# list[start:end:step]
# start => index of the first element you want to include in the slice(inclusive)
# end => index of the last element you want to include in the slice(exclusive)
# step => the interval between each element in the slice (optiional, default is 1)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice the first 3 elements
print(my_list[0:3])  # output: [0, 1, 2]

# slice elements from index 3 to index 6
print(my_list[3:7])  # output: [3, 4, 5, 6]

# slice elements from index 0 to index 9 with step 2
# step specifies the stride or interval between elements in the sliced list
# by default the step value is 1 which means that the sliced list will contain every element between the start and the end indices
# however you can set the step value to any positive or negative integer to skip elements or reverse the order of the elements
print(my_list[0:10:2])  # output: [0, 2, 4, 6, 8]

# slice elements from index 3 to the end of the list
# if last index is not specified it defaults to the length of the list
print(my_list[3:])  # output: [3, 4, 5, 6, 7, 8, 9]

# slice elements from the beginning of the list to index 5
# if start index is not specified it defaults to0
print(my_list[:6])  # output: [0, 1, 2, 3, 4, 5]

# slice the whole list
print(my_list[:])  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# slice elements from index 0 to 9 with step 2
# sliced list contains every second element starting from the first index, so it includes elements of indices 0,2,4,6 and 8
print(my_list[0:10:2])  # output: [0, 2, 4, 6, 8]

# slice elements from index 0 to 9 with step 3
# the sliced list contains every third element starting from the first index so it includes elements at indices 0,3,6 and 9
print(my_list[0:10:3])  # output: [0, 3, 6, 9]

# slice elements from index 0 to 9 with step -1 (reverse order)
# the step value is negative so the sliced list is empty because the start index is less than the end index but the step value is negative
# the step value is negative which means that the sliced list will be generated in the reverse order
# however the start index is 0 is less than the end index 10, which is invalid because the sliced list can only be generated if the start index is greater than the end index when the step value is negative
# therefore the output will be an empty list because no elements can be included in the sliced list that meets the condition of having a negative step value with a valid start and end index
print(my_list[0:10:-1])  # output: []

# slice elements from index 9 to 0 with step -1 (reverse order)
# the sliced list starts from the last index and goes backward with a step value of -1, so it includes all the elements in reverse order
print(my_list[9::-1])  # output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(my_list[9::-2])