# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. 

def reverse_words(string):
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

input_string = input("Enter a long string containing multiple words: ")
reversed_string = reverse_words(input_string)
print("The same string, except with the words in backwards order:")
print(reversed_string)