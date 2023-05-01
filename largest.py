# Implement a function that takes as input three variables, and returns the largest of the three.  five python solution

# using if else
def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
# using built in max method
def find_largest(a, b, c):
    return max(a, b, c)

# using a ternary operator
def find_largest(a, b, c):
    return a if (a > b and a > c) else (b if (b > a and b > c) else c)

# using lambda and reduce
from functools import reduce

def find_largest(a, b, c):
    return reduce(lambda x, y: x if (x > y) else y, [a, b, c])