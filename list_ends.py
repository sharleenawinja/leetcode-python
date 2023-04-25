# write a program that takes a list of numbers 
# and makes a new list of only the first and last elements of the given list


# finding first and last element using indexing
def last_and_first(num_list):
    first_element = num_list[0]
    last_element = num_list[-1]
    return [first_element, last_element]

print(last_and_first([5, 10, 15, 20, 25]))