# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

def list_overlap(first_list, second_list):
    overlapping = []
    # looping through shortest array to avoid number of iterations
    if len(first_list) > len(second_list):
        for el in second_list:
            if el in first_list:
                overlapping.append(el)
        return overlapping
    else:
        for el in first_list:
            if el in second_list:
                overlapping.append(el)
        return overlapping


print(list_overlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))   

# second method
def second_list_overlap(first_list, second_list):
    # Use a set instead of a list to store the overlapping elements. This will eliminate duplicates automatically and improve performance for large lists.
    # Instead of using an if statement to determine which list is shorter, we can use the set() function to create a set from each list and use the & operator to find the intersection of the sets. 
    # This will give us a set containing only the elements that are common to both lists, without duplicates.
    set1 = set(first_list)
    set2 = set(second_list)
    overlapping = set1 & set2
    return list(overlapping)

print(second_list_overlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

# Randomly generate two lists to test this
# Write this in one line of Python 

import random
a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 15)
overlap = list(set(a) & set(b))
print(overlap)
