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

def remove_duplicates_3(lst):
    return [item for index, item in enumerate(lst) if item not in lst[:index]]
print(remove_duplicates_3(names))

from collections import OrderedDict

def remove_duplicates_4(lst):
    return list(OrderedDict.fromkeys(lst).keys())
print(remove_duplicates_4(names))

def remove_duplicates_5(lst):
    i = 0
    while i < len(lst):
        if lst.count(lst[i]) > 1:
            lst.remove(lst[i])
        else:
            i += 1
    return lst
print(remove_duplicates_5(names))