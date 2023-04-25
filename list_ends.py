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

# getting first and last element using map and get item method
test_list = [5, 10, 15, 20, 25]  # Define the original list of numbers
index_list = [0, len(test_list) - 1]  # Define a list containing the indices of the first and last elements

res = map(test_list.__getitem__, index_list)  # Use map() to apply the __getitem__() method to the test_list at the indices in index_list
# This line uses the map() function to apply the __getitem__() method to the test_list array with each index in index_list. 
#  The __getitem__() method is a special method that gets the value of an item at a specified index, so it's perfect for our purposes.
# The map() function returns a map object, which is a generator that produces the results of the function calls one at a time.
# In this case, res is a map object that contains the first and last elements of the test_list array.

print('The original list is:', test_list)  # Print the original list

print('The first and last elements of the list are:', *res)  # Print the first and last elements of the list
# This line prints the first and last elements of the test_list array to the console. 
# The *res syntax "unpacks" the map object so that its elements are printed out as individual arguments to the print() function. 
# The result is a nicely formatted string that displays the first and last elements of the test_list array.
# So in summary, the map() function is used in combination with the __getitem__() method to extract the first and last elements of the test_list array, and the res variable stores the results of these operations as a map object.



# MAGIC METHODS
# in python there are a lot of functions that are used for particular purposes, and they have double underscores before and after the function name
# they are called magic functions or dunder functions
# example: __abs__, __contains__
# __str__() => used to return the printable string
# __add__() => used to add the two objects or attributes
# _ge__() => used to overload the greater than or equal operator(>=)
# __floor__() => this method is called by Math.floor() internally
# __ceil__() => this method is called by Math.ceil internally
# __trunc__() => this function is called by Math.trunc internally
# __init__() => this is the constructor for any class, which is called by the __new__() function
# __getitem__() => a magic method in python that is used in a class, and it gives the flexibility to any instance of the class to use the indexer operator
# So, it is used to evaluate the value of self[key] by any object or instance of the class. Let's suppose we have one object obj, then obj[key] will be equivalent to obj.__getitem(key).
# The magic method __getitem__ is basically used for accessing list items, dictionary entries, array elements etc. It is very useful for a quick lookup of instance attributes.
