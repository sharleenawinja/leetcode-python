# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

# using string reversal
def is_palindrome(string):
    # Remove all whitespace and convert to lowercase
    string = string.replace(' ', '').lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Ask the user for a string
user_input = input("Enter a string: ")
# Check if the string is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#  using for loops
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')