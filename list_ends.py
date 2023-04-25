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

# finding first and last elements using list comprehension
def first_and_last_using_comprehension(num_list):
    # (0, -1) is a tuple containing the indices of the elements we want to access from num_list
    # in this case we want to access the first element (at index 0) and the last element(at index -1)
    # the for loop iterates over the elements in the tuple (0, -1)
    # for each element in the tuple, the expression num_list[i] is evaluated with the current value of i.
    # this accesses the element of num_list at index specified by i
    # the resulting elements are added to a new list, which is created by enclosing the entire expression in square brackets
    # so [num_list[i] for i in (0, -1)] returns a new list containing the first and last element of num_list
    return [num_list[i] for i in (0, -1)]

print(first_and_last_using_comprehension([5, 10, 15, 20, 25]))