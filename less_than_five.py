# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

def less_than_five(numList):
    for num in numList:
        if num < 5:
            print(num)


less_than_five([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])