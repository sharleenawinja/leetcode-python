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
