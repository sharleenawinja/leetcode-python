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
