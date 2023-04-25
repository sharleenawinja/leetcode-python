# write a program that takes a list of numbers 
# and makes a new list of only the first and last elements of the given list


# finding first and last element using indexing
def last_and_first(num_list):
    first_element = num_list[0]
    last_element = num_list[-1]
    return [first_element, last_element]

print(last_and_first([5, 10, 15, 20, 25]))

# finding first and last element using slicing
def last_and_first_using_slicing(num_list):
    return num_list[::len(num_list)-1]

print(last_and_first_using_slicing([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(last_and_first_using_slicing([5, 10, 15, 20, 25]))
