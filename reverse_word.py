# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. 

def reverse_words(string):
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

input_string = input("Enter a long string containing multiple words: ")
reversed_string = reverse_words(input_string)
print("The same string, except with the words in backwards order:")
print(reversed_string)


# using list comprehesion
input_string = input("Enter a long string containing multiple words: ")

words = input_string.split()
reversed_words = [words[i] for i in range(len(words)-1, -1, -1)]
reversed_string = " ".join(reversed_words)

print("The same string, except with the words in backwards order:")
print(reversed_string)

# using slicing
input_string = input("Enter a long string containing multiple words: ")

words = input_string.split()
reversed_words = words[::-1]
reversed_string = " ".join(reversed_words)

print("The same string, except with the words in backwards order:")
print(reversed_string)