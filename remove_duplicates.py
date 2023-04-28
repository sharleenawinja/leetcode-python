# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
def remove_duplicates_1(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

names = ["Michele", "Robin", "Sara", "Michele"]
print(remove_duplicates_1(names))

def remove_duplicates_2(lst):
    return list(set(lst))
print(remove_duplicates_2(names))
